from django.contrib import admin
from django.urls import path
from payment import views
 
urlpatterns = [
    path('pay', views.homepage, name='pay'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('succ',views.succ,name='succ'),
]