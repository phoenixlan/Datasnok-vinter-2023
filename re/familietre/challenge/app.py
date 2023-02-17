from flask import Flask, render_template, request

from output.Bjarne1988 import Bjarne1988

app = Flask(__name__)


bjarn = Bjarne1988()

@app.route('/')
def login():
    if "X-Bjarne-Password" not in request.headers:
        return "No X-Bjarne-Password provided"
    if request.headers["X-Bjarne-Password"] == bjarn.get_password():
        return "PHOENIX{pyTHoN_1nh3r1T4nc3_15_345Y?}"
    return "Wrong password"

if __name__ == '__main__':
    app.run(debug=True)