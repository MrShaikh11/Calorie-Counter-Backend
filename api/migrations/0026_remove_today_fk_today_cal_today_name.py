# Generated by Django 4.1.7 on 2023-04-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_today'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='today',
            name='fk',
        ),
        migrations.AddField(
            model_name='today',
            name='cal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='today',
            name='name',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
