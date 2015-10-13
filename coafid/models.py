# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
import uuid
import os

# Create your models here.
def get_file_path_students(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/students', filename)


class Student(models.Model):
    '''Alumnos que están realizando algún trabajo de Experiencia Recepcional.'''
    matricula = models.CharField('Matrícula', max_length=10, unique=True)
    name = models.CharField('Nombre', max_length=50)
    lastname = models.CharField('Apellidos', max_length=50)
    image = models.FileField(upload_to=get_file_path_students, null=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def save(self):
        self.slug = slugify(str(self.matricula))
        super(Student, self).save()

    def __str__(self):
        return self.matricula


#############################################################################################
def get_file_path_masters(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/masters', filename)


class Master(models.Model):
    '''Una categoría puede pertenecer a un único idioma. Un idioma puede contener una o varias categorías registradas.'''
    personal_number = models.CharField('No. de personal', max_length=10, unique=True)
    name = models.CharField('Nombre', max_length=50)
    lastname = models.CharField('Apellidos', max_length=50)
    image = models.FileField(upload_to=get_file_path_masters, null=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Maestro'
        verbose_name_plural = 'Maestros'

    def save(self):
        self.slug = slugify(str(self.name))
        super(Master, self).save()

    def __str__(self):
        return self.personal_number

#######################################################################################################################
class Project(models.Model):
    '''Una URL está registrada dentro de una o varias subcategorías pertenecientes a una misma categoría de un idioma'''
    PROJECT_KINDS = (
        ('TS', 'Tesis'),
        ('TN', 'Tesina'),
        ('PT', 'Prático - Técnico'),
        ('MN', 'Monografía'),
    )

    name = models.CharField('Nombre del proyecto', max_length=200, unique=True)
    description = models.TextField('Descripción')
    kind = models.CharField('Tipo', max_length=2, choices=PROJECT_KINDS)
    prorogation = models.BooleanField('Prórroga', default=False)
    director = models.ForeignKey(Master, verbose_name='Director', related_name='Projects')
    coodirector = models.ForeignKey(Master, verbose_name='Coodirector', related_name='Projects2')
    reader1 = models.ForeignKey(Master, verbose_name='Lector 1', related_name='Projects3')
    reader2 = models.ForeignKey(Master, verbose_name='Lector 2', related_name='Projects4')
    student = models.ForeignKey(Student, verbose_name='Alumno', related_name='Projects5')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def save(self):
        self.slug = slugify(str(self.name))
        super(Project, self).save()

    def __str__(self):
        return self.name

class Advisory(models.Model):
    '''Cada categoría cuenta debería contar con varias subcategorías y estás a su vez sólo deben estar disponibles en los idiomas a los que se le asocie.'''
    number = models.IntegerField('Número de asesoría')
    description = models.TextField('Descripción')
    date = models.DateTimeField(auto_now_add=True)
    master = models.ForeignKey(Master, verbose_name='Otorgada por', related_name='Advisories')
    student = models.ForeignKey(Student, verbose_name='Para', related_name='Advisories2')
    project = models.ForeignKey(Project, verbose_name='Proyecto', related_name='Advisories3')
    slug = models.SlugField(max_length=3, unique=True, blank=True, null=True)


    class Meta:
        verbose_name = 'Asesoría'
        verbose_name_plural = 'Asesorías'

    def save(self):
        self.slug = self.number
        super(Advisory, self).save()

    def __str__(self):
        return self.number