# Generated by Django 4.1.7 on 2023-04-11 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_food_cal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='today',
            name='fk',
        ),
    ]
