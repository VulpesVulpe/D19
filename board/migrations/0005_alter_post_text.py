# Generated by Django 4.1.5 on 2023-01-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]