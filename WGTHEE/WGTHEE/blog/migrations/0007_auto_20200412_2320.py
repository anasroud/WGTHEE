# Generated by Django 2.2.11 on 2020-04-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200412_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='song_image',
            field=models.ImageField(default=0, upload_to='images'),
        ),
    ]
