# Generated by Django 4.0.4 on 2022-06-02 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_venue_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Venue Owner'),
        ),
    ]