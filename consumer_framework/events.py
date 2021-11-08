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

    def __init__(self, topic, key, consume=None):
        self._topic = topic
        self._key = key
        self._register_consume(consume)
        logger.info(f'Registered Event: {self._topic}, {self._key}')

    def consume(self, message):
        self._consume(**{k: v.annotation(message.value) for k, v in signature(self._consume).parameters.items()})

    def _register_consume(self, consume):
        self._schema = self._validate_args(consume)
        self._consume = consume

    @staticmethod
    def _validate_args(consume):
        param = signature(consume).parameters
        if len(param) > 1:
            raise InvalidEventArgumentError()
        if BaseModel not in list(param.values())[0].annotation.mro():
            raise InvalidEventArgumentError()
        return list(param.values())[0].annotation


class UndefinedEvent(Event):
    def consume(self, message):
        logger.warning(f'this event is undefined event. \'{message.topic}, {message.key}\'')
