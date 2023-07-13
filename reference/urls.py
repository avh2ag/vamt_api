from django.urls import path
from .views import CaseCreateView, CaseRetrieveView

urlpatterns = [
    path('cases/',
         CaseCreateView.as_view(http_method_names=['post']), name='case-create'),
    path('cases/<int:id>/',
         CaseRetrieveView.as_view(http_method_names=['get']), name='case-retrieve'),
]
