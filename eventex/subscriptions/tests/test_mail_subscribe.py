from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Ronaldo Oliveira', cpf='12345678901',
                    email='ronaldo@oliveira.com', phone='11-2456-7894')

        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'ronaldo@oliveira.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Ronaldo Oliveira', 'ronaldo@oliveira.com',
                    '12345678901', '11-2456-7894']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
