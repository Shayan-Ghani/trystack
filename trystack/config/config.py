from os import environ
 #to get the enviroment
#variables

class Config:
    ENV = environ.get("TRYSTACK_API_ENV", "production")
    DEBUG = bool(int(environ.get("TRYSTACK_API_DEBUG", "0")))
    TESTING = DEBUG
    SQLALCHEMY_DATABASE_URI = environ.get("TRYSTACK_API_DATABASE_URI", None)
    SQLALCHEMY_RECORD_MODIFICATIONS = DEBUG
    SQLALCHEMY_RECORD_QUERIES= DEBUG
    SQLALCHEMY_ECHO = DEBUG
    DEFAULT_PROJECT_STATUS= int(environ.get("TRYSTACK_API_DEFAULT_STATUS", "0"))