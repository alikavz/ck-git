from django.urls import path
from . import views


urlpatterns = [
    path('', views.Ournewview.as_view(), name='new_post'),
    path('<int:pk>/', views.Ournewdetail.as_view(), name='new_pos'), #recieve a diffrent intiger and convert it to the id of a person
    path('create/', views.Ournewcreation.as_view(), name='creation'),
    path('<int:pk>/update/', views.Ournewupdate.as_view(), name='update'),
    path('<int:pk>/deleting/', views.Ournewdelect.as_view(), name='dil'),
]

