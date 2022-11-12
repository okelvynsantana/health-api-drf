from rest_framework import serializers
from history.models import History
from images.api.serializers import HistoryImageSerializer


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"


class HistoryDetailsSerializer(serializers.ModelSerializer):
    images = HistoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = History
        fields = [
            "id_history",
            "date",
            "onset_of_symptoms",
            "duration",
            "pain_local",
            "pain_type",
            "conclusion",
            "images"
        ]
