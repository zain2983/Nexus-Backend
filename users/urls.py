from django.urls import path
from . import views
from django.urls import path
from .views import health_check

urlpatterns = [
    path("", health_check),  # Catch-all for HEAD /
    path('signup/', views.signup),
    path('login/', views.login),
]
