from rest_framework import serializers
from patient.models import Patient
from schedules.api.serializers import ScheduleDetailsSerializer
from images.api.serializers import PatientImageSerializer


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientDetailsSerializer(serializers.ModelSerializer):
    schedules = ScheduleDetailsSerializer(many=True, read_only=True)
    images = PatientImageSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id_patient',
            'name',
            'birthday',
            'address',
            'address_number',
            'neighborhood',
            'zip_code',
            'created_at',
            'document',
            'schedules',
            'images'
        ]
