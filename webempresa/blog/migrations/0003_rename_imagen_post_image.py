# Generated by Django 4.1.7 on 2023-03-08 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imagen',
            new_name='image',
        ),
    ]
