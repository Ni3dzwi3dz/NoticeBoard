from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
from logging import Formatter, INFO
import os

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

#logs

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    log_file = RotatingFileHandler('logs/notix.log', maxBytes=10240, 
        backupCount=15)
    log_file.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    log_file.setLevel(INFO)

    app.logger.addHandler(log_file)
    app.logger.setLevel(INFO)
    app.logger.info('Notix startup')

