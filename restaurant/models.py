from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

DELIVERY_STATUS_CHOICES = (
    ('pending', 'PENDING'),
    ('failed', 'FAILED'),
    ('completed', 'COMPLETED'),
)


class Meal(models.Model):
    name = models.CharField("Name of Meal", max_length=100)

    description = models.TextField("Description of Meal", blank=True, null=True)

    price = models.DecimalField("Price in Dollar", max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='meal_images', default='meal_images/default_404_image.webp')

    available = models.BooleanField(default=False)

    stock = models.IntegerField("Online Availability", default=False)

    def __str__(self):
        return f'{self.name}'


class OrderTransaction(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField('Amount Paid ($)', max_digits=64, decimal_places=2, default=0)
    status = models.CharField('Delivery Status', max_length=9, choices=DELIVERY_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField('Date Created', default=now)
