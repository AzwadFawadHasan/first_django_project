from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

#views modules = request handler


# this is where we define our view functions
#a view function takes a request and gives a response
# request handler or action
# django it's called a view, name is misleading
# in djanog the actual views are the templates




# this function takes a REQUEST OBJECT AND RETURNS A RESPONSE
#this returns a object of HttpResponse class with a string 
def say_hello(request):
    #//#return HttpResponse('HEllo world')
    x=1
    y=2
    return render(request, 'hello.html', {'name': 'Azwad' })

#now we will use the render function to render a template and return a html markup to the clinet