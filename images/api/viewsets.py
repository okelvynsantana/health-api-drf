from rest_framework import viewsets
from images.models import HistoryImage, PatientImage
from images.api.serializers import HistoryImageSerializer, PatientImageSerializer


class ImageHistoryViewSet(viewsets.ModelViewSet):
    queryset = HistoryImage.objects.all()
    serializer_class = HistoryImageSerializer


class PatientImageViewSet(viewsets.ModelViewSet):
    queryset = PatientImage.objects.all()
    serializer_class = PatientImageSerializer
