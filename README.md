# CONSUMER FRAMEWORK

## INSTALL
```
pip install consumer-framework
```

## EXAMPLE
```
# events.py
from consumer_framework import ConsumerFramework
from pydantic import BaseModel


app = ConsumerFramework()
app.config(**CONFIG)


class SomeSchema(BaseModel):
    id: str
    name: str
    description: str


@app.event(topic='some_topic', key='some_key', shcema=SomeSchema)
def some_event(message, some: SomeSchema):
    print(message.topic, message.key, message.value)
    print(some)
```

## CONFIG
https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html

## RUN
```
consumer -A events:app
```