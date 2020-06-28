# Generated by Django 3.0.7 on 2020-06-11 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillup', '0003_auto_20200611_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=65)),
                ('lname', models.CharField(max_length=65)),
                ('email', models.CharField(max_length=75)),
                ('password', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skillup.Instructor'),
        ),
    ]
