
from django.urls import include, path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.ListUserAPIView.as_view(), name="user_list"),
    path("signup/", views.UserCreateAPIView.as_view(), name="user_create"),
    path("signin/", views.UserLoginAPIView.as_view(), name="user_login"),
]