from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:zodiac_sign>/', views.get_zodiac_sign_by_number),
    path('<str:zodiac_sign>/', views.get_zodiac_sign, name=('horoscope_name')),
    path('type', views.type, name=('element_name')),
    path('type/<one_element>', views.get_sign_for_element)
]
