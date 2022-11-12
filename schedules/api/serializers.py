from rest_framework import serializers
from schedules.models import Schedule
from history.api.serializers import HistorySerializer, HistoryDetailsSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleDetailsSerializer(serializers.ModelSerializer):
    histories = HistoryDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = [
            "id_schedule",
            "schedule_datetime",
            "created_at",
            "canceled",
            "notes",
            "schedule_type",
            "histories"
        ]
