# Generated by Django 5.0.6 on 2024-05-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
