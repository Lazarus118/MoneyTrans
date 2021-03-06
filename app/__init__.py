from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Setup SQLAlchemy for the project
db = SQLAlchemy(app)

from app import views
