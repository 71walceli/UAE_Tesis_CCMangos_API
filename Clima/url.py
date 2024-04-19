from rest_framework import routers
from django.urls import path
from Clima.views import DataView


router = routers.DefaultRouter()

urlpatterns = [
    path('api/weather/data/', DataView.as_view(), name='data'),
]
urlpatterns += router.urls
