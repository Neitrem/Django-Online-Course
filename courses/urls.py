from django.urls import path, include

from . import views


app_name='courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>', views.show, name='show'),
    path('create/', views.create, name='create'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
]