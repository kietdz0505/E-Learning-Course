from django.http import HttpResponse


def index(request):
    return HttpResponse("e-Course App")


from django.shortcuts import render

# Create your views here.
