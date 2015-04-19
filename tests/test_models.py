#! ../env/bin/python
# -*- coding: utf-8 -*-
from appname import create_app
from appname.models import db, User
from flask.ext.bcrypt import check_password_hash

class TestModels:
    def setup(self):
        app = create_app(TESTING=True)
        self.app = app.test_client()
        db.app = app
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def test_user(self):
        admin = User('admin', 'supersafepassword')

        assert admin.username == 'admin'
        assert check_password_hash(admin.password, 'supersafepassword')

        db.session.add(admin)
        db.session.commit()
