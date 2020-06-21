
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

__all__ = ['models', 'routes']

app = Flask(__name__)
app.secret_key = 'abc42r2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db: SQLAlchemy = SQLAlchemy(app)
login_manager = LoginManager(app)

from forum import models, routes  # noqa: E402

db.create_all()
