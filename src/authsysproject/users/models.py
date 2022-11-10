from django.db import models

# Create your models here.
class Image(models.Model):
    # title = models.CharField(default,max_length=100)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)



class ImageShow(models.Model):
    # title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'image')
    added_date = models.DateTimeField()
    category = models.ForeignKey(Image, on_delete = models.CASCADE)