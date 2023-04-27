from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Liau liau liau!!!")

# Create your views here.
