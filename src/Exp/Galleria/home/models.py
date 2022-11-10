from django.db import models

# Create categories model

class Category(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'image')
    added_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.title