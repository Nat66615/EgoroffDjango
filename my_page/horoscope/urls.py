from django.urls import path
from . import views

urlpatterns = [
    path('<zodiac_sign>/', views.get_zodiac_sign)
    #path('leo/', views.leo),
    #path('scorpio/', views.scorpio),
]
