import os
from flask import Flask, url_for, request

app = Flask(__name__)

#GET method
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        return 'Username is '+ request.values["username"]
    else:
        return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

''' 
Lesson 1

@app.route('/')
def index():
    return url_for('show_user', username='deba')
    
@app.route('/user/<username>') #<username> will be the variable passe sin the url
def show_user(username):
    return 'Welcome %s %s'%(username, " again")
    
@app.route('/post/<int:post_id>') #the int says falsk is expecting a integer
def show_post(post_id):
    return "Post %d"%(post_id)

@app.route('/hello')
def hello_world():
    #using python debugger   
    import pdb; pdb.set_trace()
    i = 3
    i += 1
    return 'your car lovely'
'''
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    #setting degug is True, not for prod as it will slow down the app
    app.debug = True
    app.run(host=host, port=port)
    