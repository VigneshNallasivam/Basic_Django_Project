from django.shortcuts import render
from django.http import HttpResponse

def havanas(request):
    return HttpResponse("Hello from havanas!")