# Generated by Django 3.1.4 on 2021-01-02 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210102_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('publish',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
    ]
