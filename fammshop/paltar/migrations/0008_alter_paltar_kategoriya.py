# Generated by Django 4.0.6 on 2022-09-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paltar', '0007_category_paltar_kategoriya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paltar',
            name='kategoriya',
            field=models.ManyToManyField(related_name='mehsul_kategoriyasi', to='paltar.category'),
        ),
    ]
