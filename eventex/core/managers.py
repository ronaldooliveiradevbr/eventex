from django.db import models


class KindQueryset(models.QuerySet):
    def emails(self):
        return self.filter(kind=self.model.EMAIL)

    def phones(self):
        return self.filter(kind=self.model.PHONE)


class PeriodManager(models.Manager):
    NOON = '12:00'

    def in_the_morning(self):
        return self.filter(start__lt=self.NOON)

    def in_the_afternoon(self):
        return self.filter(start__gte=self.NOON)
