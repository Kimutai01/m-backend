from django.urls import path
from base.views import table_views as views

urlpatterns = [
    path('', views.getTables, name='tables'),
]
