# Generated by Django 3.2.13 on 2022-05-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProjectA', '0002_fash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fash2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fash2_img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
