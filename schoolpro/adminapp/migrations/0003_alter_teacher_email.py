# Generated by Django 5.0.4 on 2024-05-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
