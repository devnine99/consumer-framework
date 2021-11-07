import logging
from functools import wraps

from kafka import KafkaConsumer

from consumer_framework.event import Event, UnDefinedEvent
from consumer_framework.exceptions import NotRegisteredTopic

logger = logging.getLogger(__name__)


class ConsumerFramework:
    _configs: dict
    _event_registry: dict = {}

    def __init__(self, *topics, **configs):
        self._register_topic(topics)
        self._configs = configs or {}

    def run(self):
        for message in KafkaConsumer(*self._event_registry.keys(), **self._configs):
            self._get_event(message.topic, message.keys()).consume(message)

    def config(self, **configs):
        self._configs.update(configs)

    def _register_topic(self, topics):
        for topic in topics:
            self._event_registry[topic] = {}

    def event(self, *, topic, key, schema=None):
        def register_event(consume):
            try:
                self._event_registry[topic][key] = Event(topic, key, consume, schema)
            except KeyError:
                raise NotRegisteredTopic(topic)

            @wraps(consume)
            def wrapped(*args, **kwargs):
                pass
            return wrapped
        return register_event

    def _get_event(self, topic, key):
        try:
            return self._event_registry[topic][key]
        except KeyError:
            return UnDefinedEvent(topic, key)
