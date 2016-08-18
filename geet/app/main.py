import os

from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.debug = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def market():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
   
 
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))
if __name__ == "__main__":
    app.run(host=host, port=port) # host=host, port=port

