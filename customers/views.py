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
    if request.method=='POST':
        cf = CustomerForm(request.POST)
        if cf.is_valid():
            cf.save()
            return redirect(reverse('customers:list_customers'))
        return render(request, 'customers/addform.html', {
            'cf':cf,
        })

    if request.method=='GET':
        cf = CustomerForm()
        return render(request, 'customers/addform.html', {
            'cf': cf,
        })
    # TODO: a better date widget in the template
    # TODO: handle methods not allowed

def edit_customer(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return notfound(request)
    
    if request.method=='POST':
        # handle delete
        if 'delete' in request.POST:
            customer.delete()
            return redirect(reverse('customers:list_customers'))

        # populate customer record and try to save
        if 'save' in request.POST:
            cf = CustomerForm(request.POST, instance=customer)
            if cf.is_valid():
                cf.save()
                return redirect(
                    reverse('customers:edit_customer', args=(customer.id,)))
            return render('customers:editform.html', {
                'customer': customer,
                'cf': cf,
            })
            
        # else redirect

    if request.method=='GET':
        cf = CustomerForm(instance=customer)
        return render(request, 'customers/editform.html', {
            'customer':customer,
            'cf': cf,
        })
    # TODO: handle methods not allowed
    return notfound(request)
 
def notfound(request):
    return render(request, 'customers/notfound.html')

def save_form(cf, redirect_url=None):
    cf.save()
    if redirect is not None:
        return render(request, redirect_url)
