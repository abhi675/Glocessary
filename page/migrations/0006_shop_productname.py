# Generated by Django 3.1.6 on 2021-07-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_auto_20210702_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='productname',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
