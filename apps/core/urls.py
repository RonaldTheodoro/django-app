from django.urls import path

from .views import index

APP_NAME = 'core'

urlpatterns = [
    path('', index, name='index'),
]
