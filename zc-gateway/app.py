from flask import Flask, jsonify
import requests
from discovery import ZeroConfDiscovery

app = Flask(__name__)
zc_discovery = ZeroConfDiscovery()


@app.route("/services")
def services():
    res = {"services": {}}
    for a in zc_discovery.services.values():
        # a = a.split(":")
        info = requests.get(f"http://{a}/info")
        r = info.json()
        res["services"][r["name"]] = r["response"]
    return jsonify(res)


if __name__ == "__main__":

    zc_discovery.start()

    kwargs = {
        "host": "0.0.0.0",
        "port": 4999,
    }

    try:
        app.run(**kwargs)
    except (Exception, KeyboardInterrupt) as e:
        pass
