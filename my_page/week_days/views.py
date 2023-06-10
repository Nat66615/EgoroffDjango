from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

dic_week_day = {'monday': 'Понедельник!',
                'tuesday': 'Вторник!',
                'wednesday': 'Среда!',
                'thursday': 'Четверг!',
                'friday': 'Пятница!',
                'saturday': 'Суббота!',
                'sunday': 'Воскресенье!', }


def get_day_of_week(request, day_of_week: str):
    description_day = dic_week_day.get(day_of_week, None)
    if description_day:
        return HttpResponse(description_day)
    else:
        return HttpResponseNotFound(f'{day_of_week} не является днем недели')


def get_day_of_week_by_number(request, day_of_week: int):
    week = list(dic_week_day)
    if day_of_week > len(week):
        return HttpResponseNotFound(f'Неверный номер дня {day_of_week}')
    day_name = week[day_of_week - 1]
    redirect_url = reverse('name_day', args=(day_name,))
    return HttpResponseRedirect(redirect_url)


