from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def jampandu(request):
    return HttpResponse('<h1><marquee>Hai jampandu How Are You</h1></marquee>')
