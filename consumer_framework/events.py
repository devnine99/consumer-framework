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
        self._consume = consume
        self._validate_args()
        logger.info(f'Registered Event: {self._topic}, {self._key}')

    def consume(self, message):
        self._consume(**{k: v.annotation(message.value) for k, v in signature(self._consume).parameters.items()})

    def _validate_args(self):
        for k, v in signature(self._consume).parameters.items():
            if BaseModel not in v.annotation.mro():
                raise InvalidEventArgumentError(k)


class UndefinedEvent(Event):
    def consume(self, message):
        logger.warning(f'this event is undefined event. \'{message.topic}, {message.key}\'')
