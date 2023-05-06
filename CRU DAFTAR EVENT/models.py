from django.db import models

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    total_prize = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.CharField(max_length=100)
    capacity = models.IntegerField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    atlet = models.ForeignKey('Atlet', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    partner = models.ForeignKey('Atlet', on_delete=models.CASCADE, null=True, blank=True)
