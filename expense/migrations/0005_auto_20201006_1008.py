# Generated by Django 3.0.7 on 2020-10-06 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='attachments',
            field=models.FileField(upload_to='attachments/'),
        ),
    ]