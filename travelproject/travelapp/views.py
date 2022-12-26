from django.shortcuts import render
from .models import Place
from django.http import HttpResponse

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})



