# Generated by Django 5.0.2 on 2024-05-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
