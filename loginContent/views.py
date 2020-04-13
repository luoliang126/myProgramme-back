from django.shortcuts import render
from django.http import HttpRequest

def login(request):
    return HttpResponse("Hello,Login. You're at the polls index.")