# Generated by Django 4.1.7 on 2023-03-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_element_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
