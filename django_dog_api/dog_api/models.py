from django.db import models

# Create your models here.


class dog(models.Model):
    name = models.CharField(max_length=32)
    birthday = models.DateField()
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    weight = models.IntegerField()


class Food(models.Model):
    dog = models.ForeignKey(dog, on_delete=models.CASCADE)
    time_fed = models.DateTimeField()
    food_total = models.IntegerField()
