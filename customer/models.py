from django.db import models


class TimeStampedModel(models.Model):
    id = models.UUIDField(max_length=34, primary_key=True)

    class Meta:
        abstract = True


class Customer(TimeStampedModel):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
