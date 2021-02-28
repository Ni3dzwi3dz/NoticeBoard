from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#App initialization
app=Flask(__name__)
app.config.from_object(Config)

#Database init
db=SQLAlchemy()
migrate= Migrate(app,db)
db.init_app(app)

#Login
login= LoginManager(app)
login.login_view = 'login'

#Vievs
from app import routes

