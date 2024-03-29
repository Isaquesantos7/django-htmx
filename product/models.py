from django.db import models

class Product(models.Model):
    index = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.name
