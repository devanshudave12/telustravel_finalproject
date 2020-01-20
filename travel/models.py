from django.db  import models

# Create your models here.


class Destination(models.Model):

    name = models.CharField(max_length=100)   # name for images
    img = models.ImageField(upload_to='pics')   # to upload the pic
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
