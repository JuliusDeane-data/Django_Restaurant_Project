# Generated by Django 5.2.3 on 2025-06-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_meal_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='image',
            field=models.ImageField(default='meal_images/default_meal.jpg', upload_to='meal_images'),
        ),
    ]
