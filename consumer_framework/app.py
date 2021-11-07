import logging

from kafka import KafkaConsumer

from consumer_framework.events import UnDefinedEvent
from consumer_framework.routers import Router

logger = logging.getLogger(__name__)


class ConsumerFramework:
    _configs: dict
    _event_registry: dict = {}
    _default_router = Router()
    _routers = [_default_router]

    def __init__(self, **configs):
        self._configs = configs or {}

    def run(self):
        self._register_router()
        for message in KafkaConsumer(*self._event_registry.keys(), **self._configs):
            self._get_event(message.topic, message.key).consume(message)

    def config(self, **configs):
        self._configs.update(configs)

    def include_router(self, router):
        self._routers.append(router)

    def _register_router(self):
        for router in self._routers:
            for topic, events in router.registry.items():
                try:
                    self._event_registry[topic].update(events)
                except KeyError:
                    self._event_registry[topic] = dict()
                    self._event_registry[topic] = events

    def event(self, *, topic, key, schema=None):
        return self._default_router.event(topic=topic, key=key, schema=schema)

    def _get_event(self, topic, key):
        try:
            return self._event_registry[topic][key]
        except KeyError:
            return UnDefinedEvent(topic, key)
