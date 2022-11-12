from rest_framework import viewsets
from schedules.models import Schedule
from schedules.api.serializers import ScheduleSerializer, ScheduleDetailsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('schedule_datetime')
    serializer_class = ScheduleSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Schedule.objects.filter(pk=pk)
        self.serializer_class = ScheduleDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


