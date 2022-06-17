# this urls.py file is used to map a view to a url, 
#by convection we call this url
# in this module we map the urls to our view functions

from django.urls import path 
from . import views # from current folder importing the views module

#setting urlpatters to a urlpatterns array of objects
#this is a URLConf module

urlpatterns = [

    path('hello/', views.say_hello)#we first gave it a path, then we are just passing a reference to the say_hello function 


]