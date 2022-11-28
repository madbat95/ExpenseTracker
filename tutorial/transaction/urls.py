# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from transaction import views
# from .views import TransactionViewSet, api_root
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter


# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'transactions', views.TransactionViewSet,basename="transaction")

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from transaction import views

urlpatterns = [
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)