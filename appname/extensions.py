from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.login import LoginManager
from flask_assets import Environment
from flask_migrate import Migrate
from appname.models import User

# Setup flask cache
cache = Cache()

# init flask assets
assets_env = Environment()

debug_toolbar = DebugToolbarExtension()

migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = "main.login"

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
