from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='name_rectangle_url'),
    path('square/<int:width>/', views.get_square_area, name='name_square_url'),
    path('circle/<int:radius>/', views.get_circle_area, name='name_circle_url'),
    path('get_rectangle_area/<int:width>/<int:height>/', views.get_rectangle_area_redirect),
    path('get_square_area/<int:width>/', views.get_square_area_redirect),
    path('get_circle_area/<int:radius>/', views.get_circle_area_redirect),
    path('title_rectangle', views.get_title_rectangle),
    path('title_square', views.get_title_square),
    path('title_circle', views.get_title_cirkle),
]
