from rest_framework import viewsets
from patient.api.serializers import PatientSerializer, PatientDetailsSerializer
from patient.models import Patient
from rest_framework.response import Response
from rest_framework.decorators import action


class PatientsViewSets(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = Patient.objects.filter(pk=pk)
        self.serializer_class = PatientDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


