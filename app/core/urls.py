from rest_framework import routers
from .views import ListAdverts, RetrieveAdvert
from django.urls import path, include


urlpatterns = [
    path('advert-list/', view=ListAdverts.as_view(), name='advert_list'),
    path('advert/<int:pk>/', view=RetrieveAdvert.as_view(), name='advert'),
]
