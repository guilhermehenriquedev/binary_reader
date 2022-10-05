from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import (
    records,
    homeviews
)

router = DefaultRouter()

router.register(r'records', records.RecordsViewSet, basename='records')

urlpatterns = [
    path('', homeviews.index, name="index"),
    path('api/', include(router.urls)),
]
