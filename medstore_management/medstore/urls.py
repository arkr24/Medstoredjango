from django.urls import path
from medstore import views 

app_name ='medstore'

urlpatterns = [
    path('',views.index, name='index'),

    path('new_bill/',views.new_bill, name='new_bill'),
    path('sales_report/',views.sales_report, name='sales_report'),

#dealer 
    path('view_dealer/',views.view_dealer, name='view_dealer'),
    path('add_dealer/',views.add_dealer, name='add_dealer'),
    path('dealerforminsert/',views.dealerforminsert, name='dealerforminsert'),
    path('dealerformupdate/<int:foo>',views.dealerformupdate, name='dealerformupdate'),
    path('dealerformview/<int:foo>',views.dealerformview, name='dealerformview'),
    path('dealerformdelete/<int:foo>',views.dealerformdelete, name='dealerformdelete'),

#cust 
    path('view_cust/',views.view_cust, name='view_cust'),
    path('add_cust/',views.add_cust, name='add_cust'),
    path('custforminsert/',views.custforminsert, name='custforminsert'),
    path('custformupdate/<int:foo>',views.custformupdate, name='custformupdate'),
    path('custformview/<int:foo>',views.custformview, name='custformview'),
    path('custformdelete/<int:foo>',views.custformdelete, name='custformdelete'),

#med
    path('view_med/',views.view_med, name='view_med'),
    path('add_med/',views.add_med, name='add_med'),
    path('dealer_med/',views.dealer_med, name='dealer_med'),
    path('medicineforminsert/',views.medicineforminsert, name='medicineforminsert'),
    path('medformupdate/<int:foo>',views.medformupdate, name='medformupdate'),
    path('medformview/<int:foo>',views.medformview, name='medformview'),
    path('medformdelete/<int:foo>',views.medformdelete, name='medformdelete'),

    
    path('view_purchase/',views.view_purchase, name='view_purchase'),
    path('add_purchase/',views.add_purchase, name='add_purchase'),

#emp
    path('view_emp/',views.view_emp, name='view_emp'),
    path('add_emp/',views.add_emp, name='add_emp'),
    path('empforminsert/',views.empforminsert, name='empforminsert'),
    path('empformupdate/<int:foo>',views.empformupdate, name='empformupdate'),
    path('empformview/<int:foo>',views.empformview, name='empformview'),
    path('empformdelete/<int:foo>',views.empformdelete, name='empformdelete'),

    
]
