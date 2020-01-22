from django.db import models
from django import forms 

class Customer(models.Model):
    first_name = models.CharField('First name', max_length=500)
    last_name = models.CharField('Last name', max_length=500)
    phone = models.CharField('Phone', max_length=500)
    date_of_contact = models.DateField('Date of contact')

    def __str__(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, 
            last_name=self.last_name
        )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
