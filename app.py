from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
# Required to use session and flash messages (use a secure random key)
app.secret_key = 'supersecretkey'
USERNAME = 'admin'
PASSWORD = 'password'


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid Credentials. Please try again.')
    flash('Please login with `admin` and `password`.')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You were logged out.')
    return redirect(url_for('login'))


@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        flash('You need to login first.')
        return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
