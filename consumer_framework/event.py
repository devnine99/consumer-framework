import logging

from consumer_framework.exceptions import ValidationError

logger = logging.getLogger(__name__)


class Event:
    _topic = None
    _key = None
    _consume = None
    _schema = None

    def __init__(self, topic, key, consume=None, schema=None):
        self._topic = topic
        self._key = key
        self._consume = consume
        self._schema = schema
        logger.info(f'Registered Event: {self._topic}, {self._key}')

    def consume(self, message):
        self._validate(message)
        self._consume(message)

    def _validate(self, message):
        if self._schema and not self._schema(message).is_valid():
            raise ValidationError()


class UnDefinedEvent(Event):
    def consume(self, message):
        logger.warning(f'this event is undefined event. \'{self.message.key}\'')
