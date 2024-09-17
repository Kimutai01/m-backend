from django.urls import path
from base.views import team_views as views



urlpatterns = [
    path('', views.getTeams, name="teams"),
    path('create/', views.addTeam, name="team-create"),
    path('upload/', views.uploadImage, name="image-upload"),
    path('<str:pk>/', views.getTeam, name="team"),
    path('update/<str:pk>/', views.updateTeam, name="team-update"),
    path('delete/<str:pk>/', views.deleteTeam, name="team-delete"),
]
