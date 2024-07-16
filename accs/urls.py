from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.Signuphere.as_view(), name='signup'),
]

