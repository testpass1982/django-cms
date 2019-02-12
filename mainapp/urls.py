from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

import mainapp.views as mainapp

app_name = 'users'
urlpatterns = [
    path('', mainapp.index, name='index'),
]
