from functools import wraps

from consumer_framework.events import Event


class Router:
    registry: dict = {}

    def event(self, *, topic, key):
        def register_event(consume):
            return self._register_event(topic, key, consume)

        return register_event

    def _register_event(self, topic, key, consume):
        try:
            self.registry[topic][key] = Event(topic, key, consume)
        except KeyError:
            self.registry[topic] = dict()
            self._register_event(topic, key, consume)

        @wraps(consume)
        def wrapped(*args, **kwargs):
            return consume(*args, **kwargs)

        return wrapped
