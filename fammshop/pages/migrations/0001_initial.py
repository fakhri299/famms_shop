# Generated by Django 4.0.6 on 2022-09-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paltar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('qiymet', models.CharField(max_length=1000)),
                ('alici', models.CharField(max_length=100)),
                ('sekil', models.ImageField(upload_to='')),
                ('tesviri', models.TextField(blank=True, null=True)),
                ('elcatan', models.BooleanField(default=True)),
            ],
        ),
    ]
