
from django.urls import include, path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.ListTodoAPIView.as_view(), name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(), name="todo_create"),
]