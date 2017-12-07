from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ronaldo Oliveira',
            cpf='12345678901',
            email='ronaldo@oliveira.net',
            phone='11-2456-7894'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Ronaldo Oliveira', str(self.obj))

    def test_paid_default_to_False(self):
        """paid must be False by default"""
        self.assertEqual(False, self.obj.paid)
