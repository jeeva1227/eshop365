from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html",{'name':'jeeva'})

def add(request):
    a = request.POST['num1']
    b = request.POST['num2']
    res = int(a) + int(b)
   
    return render(request,'result.html', {'result': res})