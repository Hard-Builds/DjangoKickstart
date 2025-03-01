from django.urls import path

from users.views import register, profile

urlpatterns = [
    path("profile/", profile, name="user-profile"),
    path("register/", register, name="user-reg")
]
