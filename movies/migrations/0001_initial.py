# Generated by Django 2.0 on 2018-08-27 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('numberInStock', models.IntegerField()),
                ('dailyRentalRate', models.FloatField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Genres')),
            ],
        ),
    ]
