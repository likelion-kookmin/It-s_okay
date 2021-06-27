# Generated by Django 3.2.4 on 2021-06-27 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_alter_comment_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article'),
        ),
    ]