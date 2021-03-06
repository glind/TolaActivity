# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-04 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JupyterNotebooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Notebook Name')),
                ('very_custom_dashboard', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Specialty Custom Dashboard Links')),
                ('file', models.FileField(blank=True, null=True, upload_to=b'media', verbose_name=b'HTML/Jupyter Nontebook File')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Program')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Jupyter Notebooks',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=200, verbose_name=b'Link to Service')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[(b'gallery', b'Gallery'), (b'map', b'MapBox Map Layer')], max_length=255, null=True, verbose_name=b'Type of Link')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('link', models.ForeignKey(blank=True, max_length=200, on_delete=django.db.models.deletion.CASCADE, to='customdashboard.Link')),
                ('program', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramNarratives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narrative_title', models.CharField(blank=True, max_length=100, verbose_name=b'Narrative Title')),
                ('narrative', models.TextField(blank=True, verbose_name=b'Narrative Text')),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('program', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Program')),
            ],
        ),
    ]
