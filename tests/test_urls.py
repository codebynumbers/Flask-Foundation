#! ../env/bin/python
# -*- coding: utf-8 -*-
from tests import BaseTest


class TestURLs(BaseTest):

    def test_home(self):
        rv = self.app.get('/')
        assert rv.status_code == 200

    def test_login(self):
        rv = self.app.get('/login')
        assert rv.status_code == 200

    def test_logout(self):
        rv = self.app.get('/logout')
        assert rv.status_code == 302

    def test_restricted(self):
        rv = self.app.get('/restricted')
        assert rv.status_code == 302
