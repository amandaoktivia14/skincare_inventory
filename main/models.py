from django.db import models
# from django.utils.timezone import now

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)

