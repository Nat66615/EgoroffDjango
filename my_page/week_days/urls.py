from django.urls import path
from . import views

urlpatterns = [
    path('<day_of_week>/', views.get_day_of_week),
]