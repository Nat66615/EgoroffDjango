from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monday(request):
    return HttpResponse("Список дел понедельника")


def tuesday(request):
    return HttpResponse("Список дел вторника")
# Create your views here.

def get_day_of_week(request, day_of_week):
    if day_of_week == 'monday':
        return HttpResponse("Список дел понедельника")
    elif day_of_week == 'tuesday':
        return HttpResponse("Список дел вторника")
    else:
        return HttpResponseNotFound (f'{day_of_week} не является днем недели')

