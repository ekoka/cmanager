from datetime import datetime

from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Customer, CustomerForm

def list_customers(request):
    customers = Customer.objects.all()
    # TODO: pagination
    return render(request, 'customers/index.html', {
        'customers':customers,
    })

def add_customer(request):
    submitted = True if 'submitted' in request.GET else False
    if request.method=='POST':
        cf = CustomerForm(request.POST)
        if cf.is_valid():
            cf.save()
            return redirect(reverse('customers:list_customers'))
        return render(request, 'customers/form.html', {
            'cf':cf,
            'submitted': submitted,
        })

    if request.method=='GET':
        cf = CustomerForm()
        return render(request, 'customers/form.html', {
            'cf': cf,
            'submitted': submitted,
        })
    # TODO: a better date widget in the template
    # TODO: handle methods not allowed

def edit_customer(request, customer_id):
    try:
        customer = Customer.objects.get(customer_id)
    except:
        return redirect(reverse('customer:notfound'))
    if request.method=='POST':
        # populate customer record and try to save
        ...
        # else redirect

    if request.method=='GET':
        cf = CustomerForm(customer)
        submitted = True if 'submitted' in request.GET else False
        return render(request, 'customers/form.html', {
            'customer': customer,
            'cf': cf,
            'submitted': submitted,
        })
    # TODO: handle methods not allowed
 
def delete_customer(request, customer_id):
    try:
        Customer.objects.delete(customer_id)
    except: 
        return redirect(reverse('customers:notfound'))

def notfound(request):
    render(request, 'notfound.html')

