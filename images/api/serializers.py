from rest_framework import serializers
from images.models import HistoryImage, PatientImage


class HistoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryImage
        fields = '__all__'


class PatientImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientImage
        fields = '__all__'
