from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Dam, DamStatistics
from .serializers import DamSerializer, DamStatisticsSerializer

class DamViewSet(viewsets.ModelViewSet):
    queryset = Dam.objects.all()
    serializer_class = DamSerializer

    @action(detail=False, methods=['get'])
    def list_dams_by_district(self, request):
        district = request.query_params.get('district')
        dams = Dam.objects.filter(district=district)
        serializer = self.get_serializer(dams, many=True)
        return Response(serializer.data)

class DamStatisticsViewSet(viewsets.ModelViewSet):
    queryset = DamStatistics.objects.all()
    serializer_class = DamStatisticsSerializer

    @action(detail=False, methods=['get'])
    def get_highest_rainfall(self, request):
        highest_rainfall = DamStatistics.objects.order_by('-rainfall').first()
        serializer = self.get_serializer(highest_rainfall)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_date_of_highest_rainfall(self, request, pk=None):
        dam = get_object_or_404(Dam, pk=pk)
        highest_rainfall = dam.statistics.order_by('-rainfall').first()
        serializer = self.get_serializer(highest_rainfall)
        return Response(serializer.data)
