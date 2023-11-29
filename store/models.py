from django.db import models

class Artist(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField( upload_to="property_image")
    
    def __str__(self) :
        return self.name


class Song(models.Model):
    titles=models.CharField(max_length=200)
    duration=models.CharField(max_length=10)
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="property_image")
    realse_date=models.DateTimeField()

    def __str__(self) :
        return self.titles

# Create your models here.
