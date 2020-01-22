from django.db import models

# Create your models here.

class Customer(models.Model):
    last_name = models.CharField('First name', max_length=500)
    first_name = models.CharField('Last name', max_length=500)
    phone = models.CharField('Phone', max_length=500)
    date = models.DateTimeField('Date of contact')

    def __str__(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, 
            last_name=self.last_name
        )
