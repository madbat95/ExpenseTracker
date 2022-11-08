from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    path('', views.api_root),
    path('accounts/',
        views.AccountList.as_view(),
        name='account-list'),
    path('accounts/<int:pk>/',
        views.AccountDetail.as_view(),
        name='account-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)