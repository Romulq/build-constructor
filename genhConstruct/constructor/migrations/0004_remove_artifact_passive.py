# Generated by Django 4.0.5 on 2022-08-01 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0003_alter_artifact_options_alter_character_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='passive',
        ),
    ]
