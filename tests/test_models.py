#! ../env/bin/python
# -*- coding: utf-8 -*-
from flask_bcrypt import check_password_hash

from appname.models import db, User
from tests import BaseTest


class TestModels(BaseTest):

    def test_user(self):
        admin = User('admin', 'supersafepassword')

        assert admin.username == 'admin'
        assert check_password_hash(admin.password, 'supersafepassword')

        db.session.add(admin)
        db.session.commit()
