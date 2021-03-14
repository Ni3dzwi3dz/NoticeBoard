import os
from flask import url_for

class Config(object):
    #BASIC CONFIG
    DEBUG = True

    #FILEPATHS
    basedir = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_PATH= os.path.join(os.path.dirname('__main__'),'app','static','img',
                                                                    'covers')
    
    #TOP SECRET CONFIG
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3FG3h43ddSDF#$$ssdfsg'

    #DATABASE CONFIG
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
