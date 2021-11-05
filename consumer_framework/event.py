import abc
import logging

logger = logging.getLogger(__name__)


class Event(abc.ABC):
    key = None

    def __init__(self, message):
        self.message = message

    @abc.abstractmethod
    def consume(self):
        pass


class UnDefinedEvent(Event):
    def consume(self):
        logger.warning(f'this event is undefined event. \'{self.message.key}\'')
