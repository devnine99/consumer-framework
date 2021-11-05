import abc


class Event(abc.ABC):
    key = None

    def __init__(self, message):
        self.message = message

    @abc.abstractmethod
    def consume(self):
        pass


class UnDefinedEvent(Event):
    def consume(self):
        print(f'UnDefinedEvent: \'{self.message.key}\'')
