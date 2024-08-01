from django.urls import path
from . import views


urlpatterns = [
    path('signUp', views.signUp),
    path('logIn', views.logIn),
    path('test', views.test_token)
]