from django.db import models
from uuid import uuid4

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adresse = models.TextField(blank=True)
    phone_number = models.CharField(max_length=11, null=True)
    email = models.EmailField(blank=True)


class Commande(models.Model):
    numero = models.UUIDField(default=uuid4)
    client = models.ForeignKey(Client, related_name='commandes', on_delete=models.CASCADE)


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    adresse = models.CharField(max_length=200)

    # Donne une représentation de l'objet pour pouvoir le serializer (convertir d'un objet python à une structure de type dictionnaire) et le retourner à l'utilisateur
    def render(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "adresse": self.adresse
        }


class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.FloatField()
    fournisseur = models.ForeignKey(Fournisseur, related_name="produits", on_delete=models.CASCADE)


class Menu(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.FloatField()
    commande = models.ManyToManyField(Commande)
