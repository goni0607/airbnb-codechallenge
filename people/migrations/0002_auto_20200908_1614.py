# Generated by Django 3.1 on 2020-09-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
