from django.shortcuts import render
from django.http import HttpResponse

def faces(request):
    return HttpResponse("Hello world!")