from flask import Flask
from flask_cors import CORS
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
CORS(app)

app.config.from_envvar('APP_SETTINGS')
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, title='Text Generation', description='Created by Whiz IT Services', default='Flask',
          default_label='Controllers', doc='/swagger-ui',
          contact_url='https://whizit.co.in/', validate=True)

from application.resources import home
