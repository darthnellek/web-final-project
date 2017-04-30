from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'personal/home.html')
    
def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','kellenvwhetstone@gmail.com']})
    
def blog(request):
    return render(request,'personal/blog.html')