from datetime import datetime
from os import environ

from kafka import KafkaProducer
from pytz import UTC

bootstrap_servers = environ.get('BOOTSTRAP_SERVERS')
topic = environ.get('TOPIC')
value = environ.get('VALUE')
timeout_sec = environ.get('TIMEOUT_SEC', 60)
sasl_mechanism = environ.get('SASL_MECHANISM', 'PLAIN')
security_protocol = environ.get('SECURITY_PROTOCOL', 'SASL_SSL')
acks = environ.get('ACKS', 'all')
client_dns_lookup = environ.get('CLIENT_DNS_LOOKUP_CONFIG', 'use_all_dns_ips')
sasl_plain_username = environ.get('SASL_PLAIN_USERNAME')
sasl_plain_password = environ.get('SASL_PLAIN_PASSWORD')

producer = KafkaProducer(bootstrap_servers=bootstrap_servers.split(','),
                         key_serializer=str.encode,
                         value_serializer=str.encode,
                         security_protocol=security_protocol,
                         acks=acks,
                         sasl_mechanism=sasl_mechanism,
                         sasl_plain_username=sasl_plain_username,
                         sasl_plain_password=sasl_plain_password)

key = datetime.now().astimezone(UTC).strftime('%Y-%m-%d %H:%M:%S')
print('Sending record with key: %s and value: %s' % (key, value))
producer.send(topic, key=key, value=value).get(timeout=timeout_sec)
print('Record sent successfully')root@db9b6947a1af:/usr/src/app#
