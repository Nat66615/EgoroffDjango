from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def leo(request):
    return HttpResponse("Знак зодиака Лев")


def scorpio(request):
    return HttpResponse("Знак зодиака Скорпион")

def get_zodiac_sign(request, zodiac_sign):
    if zodiac_sign == 'leo':
        return HttpResponse("Знак зодиака лев......")
    elif zodiac_sign == 'scorpio':
        return HttpResponse("Знак зодиака Скорпион.....")
    elif zodiac_sign == 'taurus':
        return HttpResponse("Знак зодиака Телец.....")
    else:
        return HttpResponseNotFound(f'Знака с названием {zodiac_sign} не существует')


