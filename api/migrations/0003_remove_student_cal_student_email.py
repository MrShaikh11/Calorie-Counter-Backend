# Generated by Django 4.1.7 on 2023-03-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_email_student_name_remove_student_stuname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cal',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]