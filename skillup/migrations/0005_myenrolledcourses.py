# Generated by Django 3.0.7 on 2020-06-14 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skillup', '0004_auto_20200611_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyEnrolledCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=65)),
                ('prev_text', models.TextField(max_length=255, verbose_name='preview text')),
                ('image_url', models.CharField(max_length=2083)),
                ('level', models.CharField(max_length=65)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]