# Generated by Django 4.0.6 on 2022-09-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paltar', '0006_alter_paltar_tesvir'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='paltar',
            name='kategoriya',
            field=models.ManyToManyField(related_name='mehsul_slug', to='paltar.category'),
        ),
    ]
