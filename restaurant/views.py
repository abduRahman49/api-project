from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Fournisseur, Commande, Client, Menu, Produit
from .serializers import FournisseurSerializer
from rest_framework import status


class FournisseursAPIView(APIView):

    def get(self, request, id=None):
        """
        Retourne la liste de tous les fournisseurs.
        """
        if id is not None:
            fournisseur = get_object_or_404(Fournisseur, pk=id)
            serializer = FournisseurSerializer(fournisseur)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        fournisseurs = Fournisseur.objects.all()
        serializer = FournisseurSerializer(fournisseurs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """
        Crée un nouveau fournisseur.
        """
        print("Données entrantes", request.data)
        serializer = FournisseurSerializer(data=request.data)
        print(serializer.initial_data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(data=serializer.data)
    

    def put(self, request, id):
        """
        Modifie le fournisseur ayant pour id, celui fourni en paramètre
        """
        fournisseur = get_object_or_404(Fournisseur, pk=id)
        serializer = FournisseurSerializer(fournisseur, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(data=serializer.data)

    
    def delete(self, request, id):
        """
        Supprime le fournisseur ayant pour id, celui fourni en paramètre
        """
        fournisseur = get_object_or_404(Fournisseur, pk=id)
        serializer = FournisseurSerializer(fournisseur)
        fournisseur.delete()
        return Response(data=serializer.data)
        
