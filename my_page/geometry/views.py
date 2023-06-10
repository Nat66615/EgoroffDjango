from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def get_rectangle_area(request, width, height):
    rectangle_area = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {rectangle_area}')


def get_square_area(request, width):
    square_area = width * 4
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {square_area}')


def get_circle_area(request, radius):
    circle_area = round(3.14 * radius ** 2, 1)
    return HttpResponse(f'Площадь круга радиусом {radius} равна {circle_area}')


def get_rectangle_area_redirect(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def get_square_area_redirect(request, width):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def get_circle_area_redirect(request, radius):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
