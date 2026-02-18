from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake user storage (temporary)
users = {}

@app.route('/')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('dashboard'))
    else:
        return "Invalid username or password!"

@app.route('/register')
def register_page():
    return render_template("register.html")

@app.route('/register_user', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    users[username] = password
    return redirect(url_for('login_page'))

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)
