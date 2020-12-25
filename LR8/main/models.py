from django.db import models

class Phenomenon(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Description(models.Model):
    phen_id = models.ForeignKey(Phenomenon, on_delete=models.CASCADE)
    description = models.CharField(max_length=1500)
