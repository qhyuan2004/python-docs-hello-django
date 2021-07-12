from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, this is Modeling and Data Science department in DCI!")
