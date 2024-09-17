from django.urls import path
from base.views import fixture_views as views

urlpatterns = [
    path('', views.getFixtures, name='fixtures'),
    path('create/', views.addFixture, name='create-fixture'),
    path('upload/', views.uploadImage, name='image-upload'),
    path('<str:pk>/', views.getFixture, name='fixture'),
    path('update/<str:pk>/', views.updateFixture, name='update-fixture'),
    path('delete/<str:pk>/', views.deleteFixture, name='delete-fixture'),
]
