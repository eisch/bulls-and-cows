from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CurrentResult(models.Model):
    number = models.IntegerField(
        validators=[MaxValueValidator(9876), MinValueValidator(1023)])
    bull = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(0)])
    cow = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(0)])
    last_entered_number = models.IntegerField(
        validators=[MaxValueValidator(9876), MinValueValidator(1023)])


class Player(models.Model):
    name = models.CharField(max_length=200)
    current_result = models.ForeignKey(CurrentResult, on_delete=models.CASCADE)
