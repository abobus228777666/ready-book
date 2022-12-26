from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=25)
    email=models.EmailField()
    review=models.TextField()
    stars=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__ (self):
        return f'Отзыв написан: {self.name} <{self.email}>'