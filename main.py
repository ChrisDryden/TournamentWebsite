from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
 
app = Flask(__name__)
 
#Error handlers can be passed to seperate file
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')


@app.route('/')
def home():
    response = ''
    if not session.get('logged_in'):
        return render_template('login.html', response=response)
    else:
        return redirect(url_for('homepage'))

@app.route('/homepage')
def homepage():
	return render_template('homepage.html')

@app.route('/register', methods=['POST'])
def register():
    if not session.get('logged_in'):
        return render_template('register.html')
    else:
        return "Hello Boss!"


@app.route('/complete_registration', methods=['POST'])
def complete_registration():
    if not session.get('logged_in'):
        if request.form['password'] != '' and request.form['username'] != '':
            if request.form['password'] == request.form['confirm_password']:
                flash('Registration Successful')
                return register()
        flash('Wrong Password!')
        return register()
    else:
        return "Hello Boss!"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='127.0.0.1', port=5000)