class InvalidEventArgumentError(Exception):
    def __init__(self, arg=None):
        self.arg = arg


class UndefinedEventError(Exception):
    def __init__(self, topic, key):
        self.topic = topic
        self.key = key


class ValidationError(Exception):
    pass
