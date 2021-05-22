# Cron Kafka Producer
## Simple kafka producer 

This software built specific on purpose to produce message to topic in schedule

## Plugins

| Name | Description |
| ------ | ------ |
| KAFKA_BOOSTRAP_SERVER | Kafka boostrap server |
| KAFKA_TOPIC | Topic name |
| KAFKA_MESSAGE_KEY | Message key in string |
| KAFKA_MESSAGE_VALUE | Message payload in string |


## Docker
*Note: This docker image design to run as cronjob on kubernetes, When it finish the container will exit
```sh
docker pull takumiproducer/cron-kafka-producer:latest
docker run -e ENV=VALUE takumiproducer/cron-kafka-producer
```

## License

Apache 2.0