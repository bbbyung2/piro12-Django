# Generated by Django 2.2.9 on 2020-01-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_name',
            field=models.CharField(max_length=20),
        ),
    ]