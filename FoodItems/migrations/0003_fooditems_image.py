# Generated by Django 5.0.2 on 2024-03-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodItems', '0002_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditems',
            name='image',
            field=models.ImageField(default=1, upload_to='fooditems'),
            preserve_default=False,
        ),
    ]
