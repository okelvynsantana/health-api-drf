from rest_framework import viewsets
from history.api.serializers import HistorySerializer, HistoryDetailsSerializer
from history.models import History
from rest_framework.response import Response
from rest_framework.decorators import action


class HistoryViewSets(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        queryset = History.objects.filter(pk=pk)
        self.serializer_class = HistoryDetailsSerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

