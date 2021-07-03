from django.db import models
from django.utils import timezone


# Create your models here.
class Review(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_completed = models.DateField(default=timezone.now())
    rating = models.IntegerField(default=0)
    review = models.TextField()

    def __str__(self):
        return self.book_name
