# Generated by Django 4.1.7 on 2023-04-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_food_cal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='cal',
            field=models.IntegerField(),
        ),
    ]
