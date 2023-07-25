from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
    "apiKey": "AIzaSyDuA4tdxzaTfwRrqgbxRbcvOY-_mS8fWX4",
    "authDomain": "cs-authentication-lab.firebaseapp.com",
    "projectId": "cs-authentication-lab",
    "storageBucket": "cs-authentication-lab.appspot.com",
    "messagingSenderId": "658586384685",
    "appId": "1:658586384685:web:7f77836e36e3d54be93ba4",
    "measurementId": "G-9QKHQWV7TB",
    "databaseURL": "https://cs-authentication-lab-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password('email','password')
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication Failed"    
    return render_template("signin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        username = request.form['username']
        bio = request.form['bio']
        try: 
            login_session['user'] = auth.create_user_with_email_and_password('email', 'password')
            return redirect(url_for('add_tweet'))
        except: 
            error = "Authentication Failed"
    UID = login_session['user']['localId']
    user = {"full_name": full_name, "username": username,"email": email, "password": password, "bio": bio }
    db.child("User").child(UID).set(user)

    return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        try:
            UID = login_session['user']['localId']
            tweet = { "title": titel, "text": text, "UID": IUD}
            db.child("User").child(UID).set(user)
        except:
            error = "Authentication Failed"
            return redirect(url_for('add_tweet'))
    return render_template("add_tweet.html")

@app.route('/all_tweets', methods=['POST', 'GET'])
def all_tweets():
    tweets = db.child("user").get().val()


if __name__ == '__main__':
    app.run(debug=True)