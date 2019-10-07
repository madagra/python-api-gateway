import os
from flask import Flask, jsonify
from registration import ZeroConfRegistration

NAME = "zc-client-1" if "ZC_NAME" not in os.environ else os.environ["ZC_NAME"]
PORT = 5000 if "ZC_PORT" not in os.environ else int(os.environ["ZC_PORT"])

app = Flask(NAME)


@app.route("/info")
def info():
    res = {
        "name": NAME,
        "response": f"Hello, I am the service {NAME}"
    }
    return jsonify(res)


if __name__ == "__main__":

    # register the service
    zc_register = ZeroConfRegistration(NAME, PORT)

    kwargs = {
        "host": "0.0.0.0",
        "port": PORT
    }
    try:
        app.run(**kwargs)
    except (Exception, KeyboardInterrupt) as e:
        pass
    finally:
        # always unregister the service before terminating the application
        zc_register.unregister()
