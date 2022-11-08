from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from account import views
from .views import AccountViewSet, api_root

account_list = AccountViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
account_detail = AccountViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('accounts/', account_list, name='account-list'),
    path('accounts/<int:pk>/', account_detail, name='account-detail'),
])