import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379, decode_responses=True)


@app.route("/")
def index():
    anzahl = r.incr("hits")
    return f"<h1>Besuche: {anzahl}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
