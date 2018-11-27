# Generated by Django 2.1.3 on 2018-11-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_evento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('auspicio', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('id_evento',),
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('id_tipo',),
            },
        ),
    ]