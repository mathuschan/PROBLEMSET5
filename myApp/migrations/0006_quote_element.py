# Generated by Django 4.1.7 on 2023-04-02 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_person_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='element',
            field=models.CharField(default='default_value', max_length=255),
        ),
    ]