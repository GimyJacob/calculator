from django.http import HttpResponse
from django.shortcuts import render
from .models import fashion, Fash, Fash2


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def index(request):
    obj= fashion.objects.all()
    obj1= Fash.objects.all()
    obj2=Fash2.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1,'result2':obj2})


def manipulation(request):
    if request.method=='GET':
        x = request.GET.get('number1')
        y = request.GET.get('number2')
        S = int(x) + int(y)
        D = int(x) - int(y)
        P = int(x) * int(y)
        Q = int(x) / int(y)
    return render(request, "result.html", {'Sum': S, 'Difference': D, 'Product': P, 'Quotient': Q, 'number1':x,'number2':y})


def result(request):
    return render(request, 'manipulation.html')


def thanks(request):
    return HttpResponse('Thanks for visiting')

