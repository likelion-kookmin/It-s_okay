# Generated by Django 3.2.3 on 2021-05-31 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
    ]