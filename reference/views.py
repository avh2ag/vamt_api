from rest_framework import generics
from .models import Case
from .serializers import CaseSerializer


class CaseView(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    lookup_field = 'id'
