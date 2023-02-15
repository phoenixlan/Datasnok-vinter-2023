from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def update_text():
    if "tamagochi" in request.headers.get("User-Agent").lower():
        return json.dumps({
            "flag": "PHOENIX{H77p_h34D3rS_Y34H!}"
        })
    return json.dumps({
        "error": "Nice try, we don't support %s :)" % request.headers.get("User-Agent")[:20]
    })

@app.route('/')
def hello_default():
    return '<h1>Invalid HTTP method</h1>'


if __name__ == "__main__":
    app.run(debug=True)
