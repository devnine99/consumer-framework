from functools import wraps

from consumer_framework.events import Event


class Router:
    registry: dict = {}

    def event(self, *, topic, key, schema=None):
        def register_event(consume):
            return self._register_event(topic, key, consume, schema)

        return register_event

    def _register_event(self, topic, key, consume, schema):
        try:
            self.registry[topic][key] = Event(topic, key, consume, schema)
        except KeyError:
            self.registry[topic] = dict()
            self._register_event(topic, key, consume, schema)

        @wraps(consume)
        def wrapped(*args, **kwargs):
            return consume(*args, **kwargs)

        return wrapped
