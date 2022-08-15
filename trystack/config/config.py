from os import environ

class Config:

    ENV = environ.get("TRYSTACK_API_ENV", "production")
    DEBUG = bool(int(environ.get("TRYSTACK_API_DEBUG", "0")))
    TESTING = DEBUG
