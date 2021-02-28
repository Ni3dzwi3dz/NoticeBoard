import os

class Config(object):
    #BASIC CONFIG
    DEBUG = True

    #FILEPATHS
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    #TOP SECRET CONFIG
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3FG3h43ddSDF#$$ssdfsg'

    #DATABASE CONFIG
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
