from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index1(request):
    return HttpResponse("Hello, world111. You're at the polls index.")

def index2(request):
    return HttpResponse("Hello, world222. You're at the polls index.")
