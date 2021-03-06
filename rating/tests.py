from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.


class TestUser(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Alinur', password='lnsdgwra12')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()