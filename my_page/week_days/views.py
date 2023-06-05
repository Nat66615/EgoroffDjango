from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def monday(request):
    return HttpResponse("Список дел понедельника")


def tuesday(request):
    return HttpResponse("Список дел вторника")
# Create your views here.
