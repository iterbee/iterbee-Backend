from django.db import models

# Create your models here.

class CulturalPoint(models.Model):
    # this is technically not necessary but pycharm does not find objects unless explicitly declared
    objects = models.Manager()

    coord = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name


test1 = CulturalPoint(coord="13289", location_name="bcn", info="buenos dias")
test1.save()