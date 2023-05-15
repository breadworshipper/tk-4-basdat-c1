from django.db import models

class Qualification(models.Model):
    batch_number = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    date = models.DateField()
    atlet = models.ForeignKey('Atlet', on_delete=models.CASCADE)

class UjianKualifikasi(models.Model):
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    correct_choice = models.CharField(max_length=100)
    is_passed = models.BooleanField(default=False)
