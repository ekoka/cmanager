from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Customer, CustomerForm

def list_customers(request):
    customers = Customer.objects.all()
    # TODO: pagination
    return render(request, 'customers/list.html', {
        'customers':customers,
    })

def add_customer(request):
    submitted = True if 'submitted' in request.GET else False
    if request.method=='POST':
        cf = CustomerForm(request.POST)
        if cf.is_valid():
            cf.save()
            return redirect(reverse('customers:list_customers'))
        return render(request, 'customers/addform.html', {
            'cf':cf,
            'submitted': submitted,
        })

    if request.method=='GET':
        cf = CustomerForm()
        return render(request, 'customers/addform.html', {
            'cf': cf,
            'submitted': submitted,
        })
    # TODO: a better date widget in the template
    # TODO: handle methods not allowed

def edit_customer(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return notfound(request)
    
    submitted = True if 'submitted' in request.GET else False
    if request.method=='POST':
        # handle delete
        if 'delete' in request.POST:
            customer.delete()
            return redirect(reverse('customers:list_customers'))

        # populate customer record and try to save
        ...
        # else redirect

    if request.method=='GET':
        cf = CustomerForm(instance=customer)
        return render(request, 'customers/editform.html', {
            'customer':customer,
            'cf': cf,
            'submitted': submitted,
        })
    # TODO: handle methods not allowed
 
def notfound(request):
    return render(request, 'customers/notfound.html')

