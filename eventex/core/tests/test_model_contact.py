from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Ronaldo Oliveira', slug='ronaldo-oliveira',
                                              photo='http://hbn.net/ro-pic')

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='ronaldo@oliveira.com')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='11-23456789')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """ Contact kinds should be limited to E and P """
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='ronaldo@oliveira.com')
        self.assertEqual('ronaldo@oliveira.com', str(contact))
