# Generated by Django 2.0.6 on 2019-01-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20190105_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='date_admitted',
            field=models.DateField(help_text='Format: YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='date_of_birth',
            field=models.DateField(help_text='Format: YYYY-MM-DD'),
        ),
    ]
