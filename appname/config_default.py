DEBUG = True
ASSETS_DEBUG = False
DEBUG_TB_INTERCEPT_REDIRECTS = False

SECRET_KEY = 'secret key'

CACHE_TYPE = 'null'
CACHE_NO_NULL_WARNING = True

SQLALCHEMY_POOL_RECYCLE = 3600
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/appname/database.db'
#SQLALCHEMY_DATABASE_URI = 'mysql://appname:appname@localhost:3306/appname?charset=utf8'