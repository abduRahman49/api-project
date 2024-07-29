from rest_framework.viewsets import ModelViewSet
from .serializers import FournisseurSerializer
from .models import Fournisseur


class FournisseurViewset(ModelViewSet):

    serializer_class = FournisseurSerializer
    queryset = Fournisseur.objects.all()
    