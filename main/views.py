from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Hello</h4>")

def job(request):
    return HttpResponse("<h4>Jobs</h4>")
# Create your views here.
