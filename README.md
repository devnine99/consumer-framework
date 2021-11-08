# CONSUMER FRAMEWORK

## INSTALL
```
pip install consumer-framework
```

## USE
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
```
```

## RUN
```
consumer -A events:app
```