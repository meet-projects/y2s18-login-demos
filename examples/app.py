from flask import Flask
from flask import Flask, render_template, request, session

import databases
import os
 
app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "You're logged in {}!".format(session['username'])
 
@app.route('/login', methods=['POST'])
def login():
    user = databases.query_by_name(request.form['username'])
    if user is None:
        return render_template('failed_login.html')
    if user.password == request.form['password']:
        session['logged_in'] = True
        session['username'] = user.username
    else:
        return render_template('failed_login.html')
    return render_template('successful_login.html')
 
if __name__ == "__main__":
    app.run(debug=True)