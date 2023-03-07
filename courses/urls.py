from django.urls import path, include

from . import views


app_name='courses'

urlpatterns = [
    path('', views.courses_index, name='courses_index')
]