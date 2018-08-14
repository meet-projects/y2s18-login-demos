# y2s18-login-demos
Demos for using login with Flask

With the examples folder, you will find a demonstration of how to use flask session to manage user logins.  This will help you do things like:

* Store the username for use across multiple functions in ```app.py```
* Avoid putting the username in the URL
* In more advanced situations, store the login information in the browser cookies so that you won't have to log in again

Try running the code.

```users.db``` holds one username and password - you can discover it by running
```bash
python3 print_databases.py users.db
```

Next, run ```app.py```
```bash
python3 app.py
```

Visit the locally-hosted app URL (127.0.0.1:5000).  Try logging in, first using the wrong password, and then the correct one.

