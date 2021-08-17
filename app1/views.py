from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_fir(request):
    return render(request,'app1_first.html')


def app_string(request):
    return HttpResponse('<h1>hi this is string response</h1>')