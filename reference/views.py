from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Case
from .serializers import CaseSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CaseView(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CaseRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    lookup_field = 'id'
