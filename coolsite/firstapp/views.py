from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def lox(request):
    return HttpResponse('<h1>Text</h1>')
