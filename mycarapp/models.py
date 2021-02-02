from django.db import models
from datetime import datetime, date
from django.conf import settings
# Create your models here.
class Voiture(models.Model):
    carid = models.AutoField(primary_key=True)
    carnom = models.CharField('Nom Voiture',max_length=50)
    carsprix = models.IntegerField('Prix Voiture')
    carpassager = models.IntegerField('Passager')
    carmoteur = models.CharField('Moteur Voiture',max_length=50)
    carporte = models.IntegerField('Nbre Porte')
    carcarburant = models.CharField('Carburant Voiture',max_length=50)
    carcategorie = models.CharField('Categorie Voiture',max_length=50)
    caroption = models.CharField(max_length=100)
    carimg = models.ImageField('Image Principale Voiture',upload_to='/image/')
    carimg1 = models.ImageField('Image1 Voiture',upload_to='/image/')
    carimg2 = models.ImageField('Image2 Voiture',upload_to='/image/')
    carimg3 = models.ImageField('Image3 Voiture',upload_to='/image/')
    carimg4 = models.ImageField('Image4 Voiture',upload_to='/image/')
    def __str__(self):
        return self.carnom

    

class Reservation(models.Model):
    rsvid = models.AutoField(primary_key=True)
    voiture=models.ForeignKey("Voiture", on_delete=models.CASCADE)
    rsvlieuramassage = models.CharField('Lieux de Prise Voiture',max_length = 150)
    rsvdateramassage = models.DateTimeField('Date de Prise Voiture')
    #rsvheureramassage = models.TimeField(null=True)
    
    rsvlieuretour = models.CharField('Lieux de Retour Voiture',max_length = 150)
    rsvdateretour = models.DateTimeField('Date de Retour Voiture')
    #rsvheureretour = models.TimeField(null=True)
    
    
    rsvnomreservant = models.CharField('Nom du Reservant Voiture',max_length = 150)
    rsvprennomreservant = models.CharField('Prenom du Reservant Voiture',max_length = 150)
    rsvmailreservant = models.EmailField('Email du Reservant Voiture',max_length = 150)
    rsvphonereservant = models.IntegerField('Telephone du Reservant Voiture',)
    rsvsupinfo = models.CharField(max_length=250)
    def __str__(self):
        return self.rsvnomreservant


class Commentaire(models.Model):
    comid = models.AutoField(primary_key=True)
    comnom = models.CharField(max_length = 250)
    comprenom = models.CharField(max_length = 250)
    comemail = models.EmailField()
    comavis = models.CharField(max_length = 250)

class Inscription(models.Model):
    inscrisid = models.AutoField(primary_key=True)
    inscrisnom = models.CharField(max_length = 250)
    inscrisprenom = models.CharField(max_length = 250)
    inscrisphone = models.IntegerField()
    inscrisemail = models.EmailField()
    inscrismdp = models.CharField(max_length = 250)


    



    


    

