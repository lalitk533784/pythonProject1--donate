# Generated by Django 3.0.5 on 2023-10-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20231003_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quickenquiry',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
    ]
