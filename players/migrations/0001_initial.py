# Generated by Django 3.0.6 on 2020-07-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('history', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='player_image')),
            ],
        ),
    ]
