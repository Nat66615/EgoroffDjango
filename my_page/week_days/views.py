from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def get_day_of_week(request, day_of_week: str):
    if day_of_week == 'monday':
        return HttpResponse("Список дел понедельника")
    elif day_of_week == 'tuesday':
        return HttpResponse("Список дел вторника")
    else:
        return HttpResponseNotFound(f'{day_of_week} не является днем недели')


def get_day_of_week_by_number(request, day_of_week: int):
    if day_of_week < 8:
        return HttpResponse(f'Сегодня {day_of_week} день недели')
    else:
        return HttpResponse(f'Неверный номер дня {day_of_week}')
