# Generated by Django 5.0.2 on 2024-02-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_course_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='month',
            field=models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default='1', max_length=9),
        ),
    ]
