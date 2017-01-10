from django.test import TestCase

from account.models import Account
from mail.models import Mail


class MailMethodTests(TestCase):
    def test_write_on_database(self):
        author = Account.objects.create(email='eamil@email.email', password='55')
        m = Mail(message='Test', author=author, head='Head Test', recipient='xryssteam@gmail.com')
        self.assertEqual(m.save(), None)
