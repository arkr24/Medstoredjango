from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
# from .models import Purchase
from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse


# Create your views here.
# index 01 -------------------------------------------
def index(request):
    return render(request, 'index.html')
###---------------------------------------------------


###------------sales --------------------------------
# new bill  02
def new_bill(request):    
    return render(request, 'new_bill.html')

# sales report  03  --------------------------------
def sales_report(request):    
    return render(request, 'view_sales_report.html')
###---------------------------------------------------


###------------DEALER -------------------------------

def view_dealer(request):
    dealer = Dealer.objects.all()
    dict = {"dealer": dealer}  
    print(dealer)   
    return render(request, 'view_dealer.html', dict)

#add dealer 05
def add_dealer(request):
    dict = {'add': True, }    
    return render(request, 'add_dealer.html', dict)


def dealerforminsert(request):
    try:
        dealer = Dealer()
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        dealer.save()
    except IntegrityError:
        return HttpResponse("<script>window.alert('already exists!!!');</script>")
    return HttpResponse("<script>window.alert('SUCCESSFULLY ADDED!!!');window.location.href='/view_dealer/'</script>")



def dealerformupdate(request, foo):
    try:
        dealer = Dealer.objects.get(pk=foo)
        dealer.dname = request.POST['dname']
        dealer.address = request.POST['address']
        dealer.phn_no = request.POST['pno']
        dealer.email = request.POST['email']
        {'dealer':dealer}
        dealer.save()
    except IntegrityError:
        return HttpResponse("<script>window.alert('already exists!!!');</script>")
    return HttpResponse("<script>window.alert('SUCCESSFULLY UPDATED!!!');window.location.href='/view_dealer/'</script>")



def dealerformview(request, foo):
    dealer = Dealer.objects.get(pk=foo)
    dict = {'dealer': dealer}
    return render(request, 'add_dealer.html', dict)


def dealerformdelete(request, foo):
    dealer = Dealer.objects.get(pk=foo)
    dealer.delete()
    return HttpResponse("<script>window.alert('deleted!');window.location.href='/view_dealer/'</script>")

###------------customer-------------------------------
#view customer 12
def view_cust(request):
    cust = Customer.objects.all()
    dict = {"cust": cust}
    return render(request, 'view_customer.html',dict)

#add customer13
def add_cust(request):
    dict = {'add': True, }    
    return render(request, 'add_customer.html',dict)

def custforminsert(request):
    try:
        cust = Customer()
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return HttpResponse("<script>window.alert('already exists!!!');window.location.href='/view_cust/'</script>")
    return HttpResponse("<script>window.alert('SUCCESSFULLY ADDED!!!');window.location.href='/view_cust/'</script>")



def custformupdate(request, foo):
    try:
        cust = Customer.objects.get(pk=foo)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return HttpResponse("<script>window.alert('already exists!!!');window.location.href='/view_cust/'</script>")
    return HttpResponse("<script>window.alert('SUCCESSFULLY UPDATED!!!');window.location.href='/view_cust/'</script>")

def custformview(request, foo):
    cust = Customer.objects.get(pk=foo)
    dict = {'cust': cust}
    return render(request, 'add_customer.html', dict)

def custformdelete(request, foo):
    cust = Customer.objects.get(pk=foo)
    cust.delete()
    return HttpResponse("<script>window.alert('deleted!');window.location.href='/view_cust/'</script>")


###---------------------------------------------------



###------------medicine-------------------------------

def view_med(request):
    med = Medicine.objects.all()
    dict = {"med": med}
    return render(request, 'view_med.html',dict)

#add MEDICINE
def add_med(request):
    dict = {'add': True, }    
    dealer = Dealer.objects.all()
    print(dealer)   
    return render(request, 'add_med.html',dict)

## ## ## ## ## ## 

def dealer_med(request):
    dealer = dealer.objects.all()
    return render(request, 'add_med.html',{'dealer':dealer}
)

def medicineforminsert(request):
    try:
        med = Medicine()
        med.m_name = request.POST['m_name']
        med.dname = request.POST['dname']
        med.price = request.POST['price']
        med.mrp = request.POST['mrp']
        med.save()
    except IntegrityError:
        return HttpResponse("<script>window.alert('already exists!!!');</script>")
    return render(request, 'view_med.html')


def medformupdate(request, foo):
    try:
        med = Medicine.objects.get(pk=foo)
        med.m_name = request.POST['m_name']
        med.dname = request.POST['dname']
        med.price = request.POST['price']
        med.mrp = request.POST['mrp']
        med.save()
    except IntegrityError:
        return HttpResponse("<script>window.alert('already exists!!!');</script>")
    return HttpResponse("<script>window.alert('SUCCESSFULLY UPDATED!!!');window.location.href='/view_med/'</script>")

def medformview(request, foo):
    med = Medicine.objects.get(pk=foo)
    dict = {'med': med}
    return render(request, 'add_med.html', dict)

def medformdelete(request, foo):
    med = Medicine.objects.get(pk=foo)
    med.delete()
    return HttpResponse("<script>window.alert('deleted!');window.location.href='/view_med/'</script>")

###---------------------------------------------------


###------------purchase -------------------------------
#view purchase   08
def view_purchase(request):    
    return render(request, 'view_purchase.html')

#add purchase  09
def add_purchase(request):    
    return render(request, 'add_purchase.html')
###---------------------------------------------------




###------------EMPLOYEE-------------------------------
#view EMPLOYEE 12
def view_emp(request):
    emp = Employee.objects.all()
    dict = {"emp": emp}
    return render(request, 'view_emp.html',dict)

#add EMPLOYEE
def add_emp(request):
    dict = {'add': True, }    
    return render(request, 'add_emp.html',dict)

def empforminsert(request):
    try:
        emp = Employee()
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.phn_no = request.POST['pno']
        emp.save()
    except IntegrityError:
        return HttpResponse("<script>window.alert('hehe already exists!!!');</script>")
    return HttpResponse("<script>window.alert('added!');window.location.href='/view_emp/'</script>")


def empformupdate(request, foo):
    try:
        emp = Employee()
        emp.fname = request.POST['fname']
        emp.lname = request.POST['lname']
        emp.address = request.POST['address']
        emp.email = request.POST['email']
        emp.sal = request.POST['sal']
        emp.phn_no = request.POST['pno']
        emp.save()
    except IntegrityError:
        return HttpResponse("<script>window.alert('up already exists!!!');</script>")
    return render(request, 'view_emp.html')

def empformview(request, foo):
    emp = Employee.objects.get(pk=foo)
    dict = {'emp': emp}
    return render(request, '123_emp.html', dict)

def empformdelete(request, foo):
    emp = Employee.objects.get(pk=foo)
    emp.delete()
    return HttpResponse("<script>window.alert('deleted!');window.location.href='/view_emp/'</script>")


###---------------------------------------------------




