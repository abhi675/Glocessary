# Generated by Django 3.1.6 on 2021-07-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20210702_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
