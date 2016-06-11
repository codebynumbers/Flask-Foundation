import os
import unittest
from appname import create_app, db


class BaseTest(unittest.TestCase):
    cwd = None

    def setUp(self):
        app = create_app(TESTING=True)
        self.app = app.test_client()
        self.ctx = app.test_request_context()
        self.ctx.push()
        db.app = app
        db.create_all()
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.create_fixtures()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.remove_ctx()

    def remove_ctx(self):
        if hasattr(self, 'ctx'):
            self.ctx.pop()
            delattr(self, 'ctx')

    def create_fixtures(self):
        pass