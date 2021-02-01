from django.contrib import admin

# Register your models here.
from .models import Voiture,Reservation,Commentaire,Inscription
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('carid', 'carnom', 'carsprix', 'carpassager', 'carmoteur', 'carporte', 'carcarburant', 'carcategorie', 'caroption', 'carimg', 'carimg1', 'carimg2', 'carimg3', 'carimg4')
admin.site.register(Voiture, VoitureAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('rsvid', 'rsvlieuramassage', 'rsvdateramassage', 'rsvlieuretour', 'rsvdateretour', 'rsvnomreservant', 'rsvprennomreservant', 'rsvmailreservant', 'rsvphonereservant', 'rsvsupinfo')
admin.site.register(Reservation, ReservationAdmin)

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('comid', 'comnom', 'comprenom', 'comemail', 'comavis')
admin.site.register(Commentaire, CommentaireAdmin)

class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('inscrisid', 'inscrisnom', 'inscrisprenom', 'inscrisphone', 'inscrisemail', 'inscrismdp')
admin.site.register(Inscription, InscriptionAdmin)





 
