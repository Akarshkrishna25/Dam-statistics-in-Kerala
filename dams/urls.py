from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DamViewSet, DamStatisticsViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'dams', DamViewSet)
router.register(r'statistics', DamStatisticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('statistics/get_highest_rainfall/', DamStatisticsViewSet.as_view({'get': 'get_highest_rainfall'}), name='get_highest_rainfall'),
    path('statistics/get_date_of_highest_rainfall/<int:pk>/', DamStatisticsViewSet.as_view({'get': 'get_date_of_highest_rainfall'}), name='get_date_of_highest_rainfall'),
    path('dams/', DamViewSet.as_view({'get': 'list_dams_by_district'}), name='list_dams_by_district'),
   
]




# dam_project/urls.py

