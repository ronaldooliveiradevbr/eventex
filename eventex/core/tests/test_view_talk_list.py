from django.test import TestCase
from django.shortcuts import resolve_url as r


class TalkListGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (2, '/palestrantes/ronaldo-oliveira/'),
            (2, 'Ronaldo Oliveira'),
           (2, 'Descrição da palestra'               ),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)
