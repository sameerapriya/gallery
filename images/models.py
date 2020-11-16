from django.db import models

# Create your models here.


class Tag(models.Model):
    """ Model for Tag """
    tag = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tag


class ImageTag(models.Model):
    """ A Picture can have multiple Tags and vice versa"""
    picture = models.ImageField(upload_to='uploaded_images')
    tag = models.ManyToManyField('Tag')
