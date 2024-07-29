from django.urls import path
from .views import FournisseursAPIView

urlpatterns = [
    path('fournisseurs/', FournisseursAPIView.as_view(), name="fournisseurs"),
    path('fournisseurs/<int:id>', FournisseursAPIView.as_view(), name="fournisseur"),
]
