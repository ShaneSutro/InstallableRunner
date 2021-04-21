from redis import Redis
from rq import Queue, Worker

redis = Redis()
queue = Queue("default", connection=redis)


def listen():
    worker = Worker(queues=[queue], connection=redis)
    worker.work(with_scheduler=True)


if __name__ == "__main__":
    listen()
