# Generated by Django 4.0.4 on 2022-06-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_venue_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='owner',
            field=models.CharField(default='admin', max_length=200),
        ),
    ]