from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_assets import Environment
from flask_migrate import Migrate

from appname.models import User

# Setup flask cache
cache = Cache()

# Init flask assets
assets_env = Environment()

# Debug Toolbar
debug_toolbar = DebugToolbarExtension()

# Alembic
migrate = Migrate()

# Flask Login
login_manager = LoginManager()
login_manager.login_view = "main.login"


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
