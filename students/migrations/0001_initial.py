# Generated by Django 2.0.6 on 2018-10-31 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('other_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('mugshot', models.ImageField(upload_to='student/image/%Y/%m/%d')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Rather Not Mention')], default='male', max_length=10)),
                ('student_class', models.CharField(choices=[('jss1', 'JSS1'), ('jss2', 'JSS2'), ('jss3', 'JSS3'), ('ss1', 'SS1'), ('ss2', 'SS2'), ('ss3', 'SS3')], max_length=50)),
                ('date_of_birth', models.DateField()),
                ('date_admitted', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('address', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Student's Profile",
            },
        ),
    ]
