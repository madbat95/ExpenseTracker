from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from account import views
from .views import AccountViewSet, api_root
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet,basename="account")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

