# Generated by Django 5.0.2 on 2024-04-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0016_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('comments', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
