from django.contrib import admin
from django.urls import path,include
from bankapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('allcustomers', views.cust, name="cust"),
    path('profilenew/<int:id>', views.profile, name="profile"),
    path('alltransaction', views.trans, name="transaction"),

]