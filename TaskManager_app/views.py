from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Create your views here.
def test(request):
    return HttpResponse("Congrats, you are in TaskManager applications!")

