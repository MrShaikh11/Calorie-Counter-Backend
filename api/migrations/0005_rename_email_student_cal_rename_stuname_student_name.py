# Generated by Django 4.1.7 on 2023-03-28 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_name_student_stuname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='cal',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stuname',
            new_name='name',
        ),
    ]