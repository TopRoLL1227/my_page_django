from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('type/', views.zodiac_types, name='zodiac_types'),
    path('type/<str:element>/', views.get_zodiac_list, name='zodiac_list'),
    path('type/<str:element>/<str:sign_zodiac>/', views.get_info_zodiac_sign_by_element, name='zodiac_info_by_element'),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:sign_zodiac>/', views.get_info_zodiac_sign_by_number),
    path('<str:sign_zodiac>/', views.get_info_zodiac_sign, name='1'),
    path('', views.index),
]


