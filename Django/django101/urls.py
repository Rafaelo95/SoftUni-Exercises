from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('django102.urls')),
    path('', include('django101_admin.urls'))
]
