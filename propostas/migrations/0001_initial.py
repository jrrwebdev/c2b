# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0022_auto_20171027_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propostas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorofertado', models.DecimalField(blank=True, decimal_places=2, max_digits=19)),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.EventoCompra')),
            ],
            options={
                'verbose_name': 'proposta',
                'verbose_name_plural': 'propostas',
            },
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='propostas',
            name='situacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='propostas.Situacao'),
        ),
    ]
