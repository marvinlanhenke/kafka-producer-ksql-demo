import json
import secrets
from time import sleep, time
from random import random
from kafka import KafkaProducer
from util.logger import get_logger

logger = get_logger(__name__)


def value_serializer(data):
    return json.dumps(data).encode('utf-8')


def get_event():
    return {
        'type': 'AccountCreated',
        'payload': {
            'user_id': secrets.token_hex(16),
            'timestamp': int(time())
        },
    }


producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=value_serializer,
)

if __name__ == '__main__':
    while True:
        try:
            ack = producer.send('dev_events', value=get_event())
            ack.get()
            sleep(int(random() * 3 + 1))
        except Exception as e:
            logger.exception(e)
