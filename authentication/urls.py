from django.urls import path
from authentication import views


urlpatterns = [
    path('user', views.UserList.as_view(), name="user"),
]