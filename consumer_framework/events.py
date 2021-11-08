import logging
from inspect import signature

from pydantic.main import BaseModel

from consumer_framework.exceptions import InvalidEventArgumentError

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
        args = [message]
        if self._schema:
            args.append(self._schema(message.data))
        self._consume(*args)


class UndefinedEvent(Event):
    def consume(self, message):
        logger.warning(f'this event is undefined event. \'{message.topic}, {message.key}\'')
