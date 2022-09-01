# Generated by Django 4.0.5 on 2022-08-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0005_artifactbuild_remove_artifact_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=255, verbose_name='Название')),
                ('img', models.ImageField(help_text='.png, то есть без фона', upload_to='images/element/', verbose_name='Изображение')),
            ],
        ),
        migrations.AlterModelOptions(
            name='artifactbuild',
            options={'verbose_name': 'Артефакт сборки', 'verbose_name_plural': 'Артефакты сборки'},
        ),
        migrations.AlterModelOptions(
            name='characterbuild',
            options={'verbose_name': 'Персонаж сборки', 'verbose_name_plural': 'Персонажи сборки'},
        ),
        migrations.AlterModelOptions(
            name='weaponbuild',
            options={'verbose_name': 'Оружие сборки', 'verbose_name_plural': 'Оружие сборки'},
        ),
    ]
