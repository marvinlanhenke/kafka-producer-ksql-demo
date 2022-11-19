# Kafka-Producer KSQL Demo

Kafka-Producer (Python) creates n-messages per seconds and streams into specified topic.
KSQLDB is used to consume streaming data with filtered streams and tables.

## **Installation**

---

Simply pull the repo and run the docker-compose.yaml from root directory.

```bash
docker compose up -d
```

## **Usage**

---

As soon as the Kafka-Producer runs, start the KSQL-CLI

```bash
docker exec -it ksqldb-cli ksql http://ksqldb-server:8088
```

Execute ksql-init.sql to create streams and tables from within ksql-cli

```bash
RUN SCRIPT '/tmp/ksql-init.sql';
```

Example Queries:

```bash
SHOW STREAMS;

SELECT * FROM STREAM_EVENT_ALL EMIT CHANGES;
```

---
