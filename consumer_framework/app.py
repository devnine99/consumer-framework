from kafka import KafkaConsumer

from consumer_framework.event import Event, UnDefinedEvent


class Consumer:
    topic: str
    configs: dict
    event_classes_registry: dict = {}

    def __init__(self, topic, **configs):
        self.topic = topic
        self.configs = configs or {}

    def run(self):
        print('registered events:')
        for event_class in self.event_classes_registry:
            print(f'- {event_class}')

        for message in KafkaConsumer(self.topic, **self.configs):
            self.get_event(message).consume()

    def config(self, **configs):
        self.configs.update(configs)

    def discover_event(self, *event_classes):
        for event_class in event_classes:
            if not self.validate_class(event_class):
                print(f'\'{event_class.__name__}\' is not Event class')
                continue
            self.event_classes_registry.update({event_class.key: event_class for event_class in event_classes})

    def get_event(self, message):
        try:
            return self.event_classes_registry[message.key](message)
        except KeyError:
            return UnDefinedEvent(message)

    @staticmethod
    def validate_class(event_class):
        if Event in event_class.mro():
            return True
        return False
