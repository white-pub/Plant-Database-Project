from django.db import models

# Create your models here.

class Plant(models.Model):
    genus = models.CharField("genus", max_length= 256)
    species = models.CharField("species", max_length= 256)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.genus} {self.species}"

