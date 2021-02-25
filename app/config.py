import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '3FG3h43ddSDF#$$ssdfsg'
    DEBUG = True
