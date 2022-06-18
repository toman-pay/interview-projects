from django.urls import path
from transaction import views

urlpatterns = [
    path('list', views.TransactionDetailsView.as_view(), name='transaction list'),
]
