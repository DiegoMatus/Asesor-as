from django.contrib import admin
from .models import Student, Master, Advisory, Project

# Register your models here.
admin.site.register(Student)
admin.site.register(Master)
admin.site.register(Advisory)
admin.site.register(Project)