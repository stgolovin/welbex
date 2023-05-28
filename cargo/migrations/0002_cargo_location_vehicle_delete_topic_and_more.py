# Generated by Django 4.2.1 on 2023-05-26 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=5)),
                ('loadcapacity', models.IntegerField()),
                ('currentlocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='cargo.location')),
            ],
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AddField(
            model_name='cargo',
            name='delieverylocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargos_delievery', to='cargo.location'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='pickuplocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargos_picup', to='cargo.location'),
        ),
    ]
