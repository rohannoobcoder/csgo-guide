# Generated by Django 3.0.6 on 2020-07-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='history',
            field=models.TextField(),
        ),
    ]
