from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config: {
    
  "apiKey": "AIzaSyDuA4tdxzaTfwRrqgbxRbcvOY-_mS8fWX4",
  "authDomain": "cs-authentication-lab.firebaseapp.com",
  "projectId": "cs-authentication-lab",
  "storageBucket": "cs-authentication-lab.appspot.com",
  "messagingSenderId": "658586384685",
  "appId": "1:658586384685:web:7f77836e36e3d54be93ba4",
  "measurementId": "G-9QKHQWV7TB"
  "databaseURL" : ""

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)