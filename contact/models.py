from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .constant import NumberType


# Create your models here.

class Audit(models.Model):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return self.name

    def delete_absolute_url(self):
        return reverse("contact:delete", kwargs={"contact_id": self.pk})


class PhoneNumber(models.Model):
    number = models.CharField(max_length=200, null=False, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=False, blank=True,
                                related_name='phone')
    type = models.CharField(max_length=50, choices=NumberType.choice())

    class Meta:
        db_table = 'phone_number'

    def __str__(self):
        return self.number
