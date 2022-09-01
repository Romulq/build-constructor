# Generated by Django 4.0.5 on 2022-08-01 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TypeArtifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TypeWeapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructor.typeweapon', verbose_name='Тип оружия')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterBuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifacts', models.ManyToManyField(to='constructor.artifact', verbose_name='Артефакты')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.character', verbose_name='Персонаж')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructor.weapon', verbose_name='Оружие')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructor.typeweapon', verbose_name='Тип оружия'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='constructor.typeartifact', verbose_name='Тип артефакта'),
        ),
    ]