# Generated by Django 4.2.1 on 2023-05-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0003_alter_location_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='weight',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='loadcapacity',
            field=models.PositiveIntegerField(),
        ),
    ]
