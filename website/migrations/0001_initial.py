# Generated by Django 4.0 on 2022-01-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=1000)),
                ('alfabeto', models.CharField(max_length=200)),
                ('estados', models.CharField(max_length=200)),
                ('estadoinicial', models.CharField(max_length=200)),
                ('estadodeaceitacao', models.CharField(max_length=200)),
                ('transicoes', models.CharField(max_length=8000)),
            ],
        ),
        migrations.CreateModel(
            name='MaquinaTuring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=1000)),
                ('estados', models.CharField(max_length=200)),
                ('estadoinicial', models.CharField(max_length=200)),
                ('estadodeaceitacao', models.CharField(max_length=200)),
                ('transicoes', models.CharField(max_length=8000)),
            ],
        ),
    ]
