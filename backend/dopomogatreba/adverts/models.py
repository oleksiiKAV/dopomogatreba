from django.db import models

# Create your models here.
class Advert(models.Model):
# model Advert 
# title - charfield 
# image - filefield 
# description - textField

    title = models.CharField(verbose_name="Название",
                            max_length=100,
                            blank=True,
                            null=True)
    image = models.FileField(verbose_name="Логотип",
                            max_length=100,
                            blank=True,
                            null=True)
    description = models.CharField(verbose_name="Описание",
                            max_length=100,
                            blank=True,
                            null=True)
    
    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        
    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Названия"
