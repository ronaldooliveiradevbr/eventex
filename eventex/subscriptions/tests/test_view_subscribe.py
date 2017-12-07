from django.core import mail
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """HTML must contain input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """HTML must contain CSRF"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must contain subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):
    """
    Cenário de sucesso: Inscrição

    Dado que um visitante acessa /inscricao/
    Quando ele preenche o formulário
         e nome, cpf, email e telefone são informados
         e ele clica em Enviar
    Então o sistema envia um e-mail de confirmação
        e o remetente é contato@eventex.com.br
        e o destinatário é o visitante
        e o remetente está em cópia carbono
        e o visitante é redirecionado para /inscricao/
        e o visitante vê uma mensagem de sucesso.
    """
    def setUp(self):
        data = dict(name='Ronaldo Oliveira', cpf='12345678901',
                    email='ronaldo@oliveira.com', phone='11-2456-7894')

        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid post should redirect to /inscricao/"""
        self.assertRedirects(self.resp, '/inscricao/1/')

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid post should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())
