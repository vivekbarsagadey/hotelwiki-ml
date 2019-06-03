from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

app = Flask(__name__)
CORS(app)

app.config.from_envvar('APP_SETTINGS')

api = Api(app, title='Basic App', description='Created by Amol Jagadambe', default='Flask', default_label='Controllers',
          validate=True)

from application.resources import home
