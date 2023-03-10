from django.urls import path, include

from . import views


app_name='courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>', views.show, name='show')
]