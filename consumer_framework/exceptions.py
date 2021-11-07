class NotRegisteredTopic(Exception):
    def __init__(self, topic):
        self.topic = topic


class ValidationError(Exception):
    pass
