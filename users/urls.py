from django.urls import path

from users.views import register, user_home

urlpatterns = [
    path("", user_home, name="user-home"),
    path("register/", register, name="user-reg")
]
