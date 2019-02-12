from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('detailview/<slug:content>/<slug:pk>', mainapp.details, name='detailview'),
]
