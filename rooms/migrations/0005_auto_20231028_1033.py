# Generated by Django 2.2.5 on 2023-10-28 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20231028_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='rooms.Amenity'),
        ),
        migrations.AddField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='rooms.Facilitie'),
        ),
        migrations.AddField(
            model_name='room',
            name='house_rules',
            field=models.ManyToManyField(blank=True, to='rooms.HouseRule'),
        ),
    ]
