from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'system/base.html')

def login(request):
    return render(request, 'system/login.html')