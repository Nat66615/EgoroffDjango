from django.urls import path
from . import views

urlpatterns = [
    path('<str:zodiac_sign>/', views.get_zodiac_sign),
    path('<str:zodiac_sign>/', views.get_zodiac_sign)

]
