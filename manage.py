#!/usr/bin/env python
from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from appname import create_app
from appname.models import db, User

app = create_app()

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """
    return dict(app=app, db=db, User=User)


if __name__ == "__main__":
    manager.run()
