# Generated by Django 4.1.7 on 2023-03-19 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='element',
            old_name='name',
            new_name='value',
        ),
    ]