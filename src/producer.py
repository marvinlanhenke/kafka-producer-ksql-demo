import os
import json
import uuid
from time import sleep, time
from random import random
from kafka import KafkaProducer
from util.logger import get_logger

logger = get_logger(__name__)


def value_serializer(data):
    return json.dumps(data).encode('utf-8')


def get_event():
    types = ['AccountCreated', 'AccountDeleted']

    return {
        'id': str(uuid.uuid4()),
        'type': types[int(random() * 2)],
        'payload': {
            'user_id': str(uuid.uuid4()),
            'timestamp': int(time())
        },
    }


producer = KafkaProducer(
    bootstrap_servers=[os.environ['BOOTSTRAP_SERVERS']],
    value_serializer=value_serializer,
)

if __name__ == '__main__':
    while True:
        try:
            for _ in range(int(os.environ['NUM_MESSAGES'])):
                ack = producer.send('dev_events', value=get_event())
                ack.get()
            sleep(1)
        except Exception as e:
            logger.exception(e)
