from django.db import models

# Create your models here.

class contactFormModel(models.Model):
    username = models.CharField(max_length=50, verbose_name="Adınız soyadınız")
    message = models.TextField(max_length=200, verbose_name="Mesajınız")
    
    def __str__(self):
        return self.username