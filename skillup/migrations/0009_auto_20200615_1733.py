# Generated by Django 3.0.7 on 2020-06-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillup', '0008_myenrolledcourses_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='vid_url',
            field=models.CharField(max_length=2083),
        ),
    ]
