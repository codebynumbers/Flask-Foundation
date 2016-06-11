#! ../env/bin/python
# -*- coding: utf-8 -*-
from appname.models import db, User
from tests import BaseTest


class TestForm(BaseTest):

    def create_fixtures(self):
        admin = User('admin', 'supersafepassword')
        db.session.add(admin)
        db.session.commit()

    def test_user_login(self):
        rv = self.app.post('/login', data=dict(
            username='admin',
            password="supersafepassword"
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'Logged in successfully.' in rv.data
