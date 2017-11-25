import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'your mom is lovely'
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port)
    