# Generated by Django 4.1.7 on 2023-04-01 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_email_student_cal_rename_stuname_student_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Food',
        ),
    ]