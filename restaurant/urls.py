from django.urls import path
# from .views import FournisseursAPIView
from .custom_viewsets import FournisseurViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'fournisseurs', FournisseurViewset, basename="fournisseur")

urlpatterns = router.urls

"""
    urlpatterns = [
    path('fournisseurs/', FournisseursAPIView.as_view(), name="fournisseurs"),
    path('fournisseurs/<int:id>', FournisseursAPIView.as_view(), name="fournisseur"),
]
"""

