import time
import os
import redis
from flask import Flask


app = Flask(__name__)
redis_server = os.getenv('REDIS')
print(redis_server) 
cache = redis.Redis(host=redis_server, port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Bem-Vindo! Você já visitou esse site {} vezes.\n'.format(count)
