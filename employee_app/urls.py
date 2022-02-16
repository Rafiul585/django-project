from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('edit/<id>', views.edit, name='show')

]
