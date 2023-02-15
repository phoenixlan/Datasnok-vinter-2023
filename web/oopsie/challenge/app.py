from flask import Flask, render_template, request

import json
import uuid
from datetime import datetime

app = Flask(__name__)

# A simple database of usernames and passwords for demonstration purposes

class User():
    def __init__(self, uuid, username, password):
        self.uuid = uuid
        self.username = username
        self.password = password
        self.last_login = datetime.now()

    def __json__(self):
        return json.dumps({
            "uuid": str(self.uuid),
            "username": self.username,
            "password": self.password,
            "last_login": int(self.last_login.timestamp())
        })

users = {
    'bjarne': User(uuid.uuid4(), "bjarne", "bjarne1234567")
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    
    if username in users:
        user = users[username]
        if password == user.password:
            return "PHOENIX{54N1712e_y0Ur_Err0R2}"
        else:
            return "ERROR: Password didn't match for user \"%s...\"" % user.__json__()[:100]
    else:
        return "Invalid "

if __name__ == '__main__':
    app.run(debug=True)