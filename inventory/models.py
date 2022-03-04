import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    serial = models.UUIDField(default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default=None)
    manufactured = models.DateField()

    def __str__(self):
        return self.name