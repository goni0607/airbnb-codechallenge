# Generated by Django 4.1.1 on 2022-09-18 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_auto_20200908_1628"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="movie",
            options={"ordering": ["-created_at"]},
        ),
    ]