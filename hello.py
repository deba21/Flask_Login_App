import os
import logging
from logging.handlers import RotatingFileHandler
import pymysql
from flask import Flask, url_for, request, render_template, redirect, flash, session    

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
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = 'Username and Password donot match'
            app.logger.warning("Incorrect username and password for use %s",
                        request.form.get('username'))
            
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    
@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

def valid_login(username, password):
    # mysql
    MYSQL_DATABASE_HOST = os.getenv('IP', '0.0.0.0')
    MYSQL_DATABASE_USER = 'deba0621'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'my_flask_app_1'
    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST,
        user=MYSQL_DATABASE_USER,
        passwd=MYSQL_DATABASE_PASSWORD,
        db=MYSQL_DATABASE_DB
        )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username='%s' AND password='%s'"%(username,password)) 
    data = cursor.fetchone()
    
    if data:
        return True
    else:
        return False
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    #setting degug is True, not for prod as it will slow down the app
    app.debug = True
    app.secret_key = '\xd4\x90*\x05\xae\x81\x84\xd8c\xaa\xaa\xc45\xa2\xc9\xa2\xbf\x04t^\x12\x13s\x8e' #os.urandom(24)
    
    #Logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    
    app.run(host=host, port=port)
    
    
    
    
    