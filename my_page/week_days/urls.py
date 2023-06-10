from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_of_week>/', views.get_day_of_week_by_number),
    path('<str:day_of_week>/', views.get_day_of_week, name='name_day'),
]