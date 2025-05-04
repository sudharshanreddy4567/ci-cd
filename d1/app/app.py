# app/app.py
from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis by container name
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f"Hello from Flask! You have visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
