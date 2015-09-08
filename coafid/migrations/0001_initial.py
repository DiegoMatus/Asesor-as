# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import coafid.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('number', models.IntegerField(verbose_name='Número de asesoría')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(null=True, blank=True, unique=True, max_length=3)),
            ],
            options={
                'verbose_name': 'Asesoría',
                'verbose_name_plural': 'Asesorías',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('personal_number', models.CharField(verbose_name='No. de personal', unique=True, max_length=10)),
                ('name', models.CharField(verbose_name='Nombre', max_length=50)),
                ('lastname', models.CharField(verbose_name='Apellidos', max_length=50)),
                ('image', models.FileField(null=True, upload_to=coafid.models.get_file_path_masters)),
                ('slug', models.SlugField(null=True, blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Maestro',
                'verbose_name_plural': 'Maestros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Nombre del proyecto', unique=True, max_length=200)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('kind', models.CharField(verbose_name='Tipo', max_length=2, choices=[('TS', 'Tesis'), ('TN', 'Tesina'), ('PT', 'Prático - Técnico'), ('MN', 'Monografía')])),
                ('prorogation', models.BooleanField(verbose_name='Prórroga', default=False)),
                ('slug', models.SlugField(null=True, blank=True, unique=True, max_length=200)),
                ('coodirector', models.ForeignKey(to='coafid.Master', verbose_name='Coodirector', related_name='Projects2')),
                ('director', models.ForeignKey(to='coafid.Master', verbose_name='Director', related_name='Projects')),
                ('reader1', models.ForeignKey(to='coafid.Master', verbose_name='Lector 1', related_name='Projects3')),
                ('reader2', models.ForeignKey(to='coafid.Master', verbose_name='Lector 2', related_name='Projects4')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('matricula', models.CharField(verbose_name='Matrícula', unique=True, max_length=10)),
                ('name', models.CharField(verbose_name='Nombre', max_length=50)),
                ('lastname', models.CharField(verbose_name='Apellidos', max_length=50)),
                ('image', models.FileField(null=True, upload_to=coafid.models.get_file_path_students)),
                ('slug', models.SlugField(null=True, blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='student',
            field=models.ForeignKey(to='coafid.Student', verbose_name='Alumno', related_name='Projects5'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advisory',
            name='master',
            field=models.ForeignKey(to='coafid.Master', verbose_name='Otorgada por', related_name='Advisories'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advisory',
            name='project',
            field=models.ForeignKey(to='coafid.Project', verbose_name='Proyecto', related_name='Advisories3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advisory',
            name='student',
            field=models.ForeignKey(to='coafid.Student', verbose_name='Para', related_name='Advisories2'),
            preserve_default=True,
        ),
    ]
