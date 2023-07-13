from django.urls import path
from .views import CaseView, CaseRetrieveUpdateView

urlpatterns = [
    path('cases/', CaseView.as_view(), name='case-list-create'),
    path('cases/<int:id>/',
         CaseRetrieveUpdateView.as_view(), name='case-retrieve-update'),
]
