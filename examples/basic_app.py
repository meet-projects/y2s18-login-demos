from flask import Flask
from flask import Flask, render_template, request, session
import os
 
app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "You're logged in!"
 
@app.route('/login', methods=['POST'])
def basic_login():
    if (request.form['password'] == 'password' and 
        request.form['username'] == 'admin'):
        session['logged_in'] = True
    else:
        return render_template('failed_login.html')
    return render_template('successful_login.html')
 
if __name__ == "__main__":
    app.run(debug=True)
