from django.shortcuts import render
from django.http import HttpResponse


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
