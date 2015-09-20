from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Game(models.Model):
	title = models.CharField(max_length=100, blank=False, default='')
	gamePicUrl = models.URLField(max_length=200, default='http://www.google.com')
	pic1Url = models.URLField(max_length=200, default='http://www.google.com')
	pic2Url = models.URLField(max_length=200, default='http://www.google.com')
	pic3Url = models.URLField(max_length=200, default='http://www.google.com')
	publisher = models.CharField(max_length=100, blank=False, default='')
	publishedDate = models.DateField()
	ratedInfo = models.CharField(max_length=100, blank=False, default='')
	gameCats = models.CharField(max_length=100, blank=False, default='')
	trailerUrl = models.URLField(max_length=200)
	buyUrl = models.URLField(max_length=200)
	rating = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(10)])
	pricing =  models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(1000)], default=250.0)
	class Meta:
		ordering = ('publishedDate',)


