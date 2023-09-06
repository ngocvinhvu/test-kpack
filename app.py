from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, everyone'

@app.route('/hello/<username>')
def hello_user(username):
    # say hello to that user
    return 'Hello %s' % escape(username)
