from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboardpage, name='app-home'),
]