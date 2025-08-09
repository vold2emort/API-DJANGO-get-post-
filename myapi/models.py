from django.db import models

# Create your models here.
class Item(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity = models.IntegerField()

    def __str__(self):
        return f"{self.Name} - {self.Price} - {self.Quantity}"