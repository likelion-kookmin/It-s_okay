# Generated by Django 3.2.4 on 2021-06-27 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20210627_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.article'),
        ),
    ]