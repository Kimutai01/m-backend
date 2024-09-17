from django.urls import path
from base.views import match_views as views

urlpatterns = [
    path('', views.getMatches, name='matches'),
    path('create/', views.addMatch, name='create-match'),
    path('upload/', views.uploadImage, name='image-upload'),
    path('<str:pk>/', views.getMatch, name='match'),
    path('update/<str:pk>/', views.updateMatch, name='update-match'),
    path('delete/<str:pk>/', views.deleteMatch, name='delete-match'),
]
