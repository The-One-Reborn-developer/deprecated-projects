# TripleTrip POI

A [TG bot](https://t.me/triple_trip_bot) for sharing points of interest with other users.

## FEATURES

- Add points of interest for moderation
- Look for points of interest
- Admin panel for moderating user posts

## DEPENDENCIES

- [aiogram](https://github.com/aiogram/aiogram)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
- [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server)
- [Docker](https://github.com/docker/docker)
- [docker-compose](https://github.com/docker/compose)

## Langueages

- English
- Russian

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
sudo docker-compose build --no-cache && sudo docker-compose up
```
