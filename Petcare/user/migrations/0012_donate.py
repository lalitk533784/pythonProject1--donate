# Generated by Django 4.2.5 on 2023-10-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_adoptform_id_alter_contacts_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donfullname', models.CharField(max_length=255)),
                ('donemail', models.CharField(max_length=255)),
                ('don_amaunt', models.CharField(max_length=255)),
                ('donpaymethod', models.CharField(max_length=255)),
            ],
        ),
    ]
