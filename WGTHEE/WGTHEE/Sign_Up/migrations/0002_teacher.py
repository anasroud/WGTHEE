# Generated by Django 3.1.3 on 2020-12-16 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Sign_Up', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_of_study', models.CharField(max_length=255)),
                ('graduation_year', models.DateTimeField()),
                ('Created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
