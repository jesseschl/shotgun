from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    shotguns_owed = models.IntegerField(default=0)
    shotguns_taken = models.IntegerField(default=0)

    def __str__(self):
        return self.name
