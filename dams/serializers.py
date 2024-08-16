from rest_framework import serializers
from .models import Dam, DamStatistics

class DamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dam
        fields = ['id', 'name', 'district']

class DamStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamStatistics
        fields = ['id', 'dam', 'date', 'rainfall', 'inflow', 'power_house_discharge', 'spillway_release']