from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse("Hello {}".format(nome))

def soma(request, val1, val2):
    return HttpResponse("O valor da soma é {}".format(val1+val2))