# Generated by Django 3.1.3 on 2020-11-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
