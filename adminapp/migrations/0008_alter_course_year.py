# Generated by Django 5.0.2 on 2024-02-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_course_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th')]),
        ),
    ]
