from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    path('users/POST', views.UserCreate.as_view()),
    path('users/GET', views.UserList.as_view()), # new
    path('users/<int:pk>/', views.UserDetail.as_view()), # new
]

urlpatterns = format_suffix_patterns(urlpatterns)