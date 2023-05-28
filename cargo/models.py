from django.db import models

# Определяем модели Cargo, Vehicle, Location, которые будут использоваться в нашем приложении.
class Cargo(models.Model):
    pickuplocation = models.ForeignKey(to='Location', on_delete=models.CASCADE, related_name='cargos_picup')
    delieverylocation = models.ForeignKey(to='Location', on_delete=models.CASCADE, related_name='cargos_delievery')
    weight = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.description}: {self.weight}"


class Vehicle(models.Model):
    uuid = models.CharField(max_length=5, unique=True)
    currentlocation = models.ForeignKey(to='Location', on_delete=models.CASCADE, related_name='vehicles')
    loadcapacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.uuid}"


class Location(models.Model):
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.city}, {self.state}"
