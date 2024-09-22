# Generated by Django 5.1.1 on 2024-09-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0002_productos_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
