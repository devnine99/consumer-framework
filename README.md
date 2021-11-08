# CONSUMER FRAMEWORK

## INSTALL
```
pip install consumer-framework
```

## EXAMPLE
```
# events.py
from consumer_framework import ConsumerFramework


app = ConsumerFramework()
app.config(**CONFIG)


@app.event(topic='some_topic', key='some_key', schema=SomeSchema)
def some_event(message):
    print(message.topic, message.key, message.value) 
```

## CONFIG
https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html

## RUN
```
consumer -A events:app
```