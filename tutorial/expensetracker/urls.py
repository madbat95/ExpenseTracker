from django.urls import path
from expensetracker import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('expensetracker/', views.user_list.as_view()),
    path('expenstracekr/<int:pk>/', views.user_detail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
