#! ../env/bin/python
from fifty.tables import FiftyTables
import os
import sys
import logging
from fifty.flask.app import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from appname import assets
from appname.models import db

from appname.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager,
    migrate
)


def create_app(config='', **config_kwargs):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        config: the path of config file
        config_kwargs: overrides

    Default config read from appname/config_default.py
    See FiftyFlask docs
    """

    app = Flask(__name__)
    config = config if os.path.isfile(config) else None
    app.configure(config, **config_kwargs)

    # Cache
    cache.init_app(app)

    # Logging
    app.logger.addHandler(logging.StreamHandler(sys.stderr))

    # Debug toolbar
    debug_toolbar.init_app(app)

    # SQLAlchemy
    db.init_app(app)

    # Flask Login
    login_manager.init_app(app)

    # FiftyTables
    FiftyTables(app)

    # Alembic
    migrate.init_app(app, db)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().iteritems():
        assets_env.register(name, bundle)

    # Register our blueprints
    from controllers import main, widgets
    app.register_blueprint(main.main_bp)
    app.register_blueprint(widgets.widgets_bp)

    # Jinja extensions
    app.jinja_env.add_extension('jinja2.ext.do')
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
