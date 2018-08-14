from flask import Flask
from flask import Flask, render_template, request

from flask import session as login_session

import databases
import os
 
app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def home():
    if not login_session.get('logged_in'):
        return render_template('login.html')
    else:
        return "You're logged in {}!".format(login_session['username'])
 
@app.route('/login', methods=['POST'])
def login():
    user = databases.query_by_name(request.form['username'])
    if user is None:
        return render_template('failed_login.html')
    if user.password == request.form['password']:
        login_session['logged_in'] = True
        login_session['username'] = user.username
    else:
        return render_template('failed_login.html')
    return render_template('successful_login.html')
 
if __name__ == "__main__":
    app.run(debug=True)