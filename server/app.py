from flask import Flask, redirect, url_for, request
from flask_cors import *
from api.user import extend
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(extend, url_prefix='/')

if __name__ == '__main__':
    app.run()


