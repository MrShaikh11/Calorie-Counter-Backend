# Generated by Django 4.1.7 on 2023-04-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_today_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='today',
            name='fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.food'),
        ),
    ]
