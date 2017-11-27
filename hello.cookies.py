import os
from flask import Flask, url_for, request, render_template, redirect, flash, make_response    

app = Flask(__name__)


#templates
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name_template=name)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method=='POST':
        if valid_login(request.form['username'], request.form['password']): 
            flash("Successfully Logged in")
            #return redirect(url_for('welcome', username=request.form.get('username')))
            #For using cookies
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('username', request.form.get('username')) #name, value
            return response
        else:
            error = 'Username and Password donot match'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0) #name, space, expires
    return response

@app.route('/')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))

def valid_login(username, password):
    if username==password:
        return True
    else:
        return False
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    #setting degug is True, not for prod as it will slow down the app
    app.debug = True
    app.secret_key = 'secretkey9827398217@^%!382!@&^#&938'
    app.run(host=host, port=port)
    