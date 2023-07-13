from rest_framework import generics
from .models import Case
from .serializers import CaseSerializer


class CaseCreateView(generics.CreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseRetrieveView(generics.RetrieveAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    lookup_field = 'id'
