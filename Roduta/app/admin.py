from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Professor, Subject, Schedule, Student

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Schedule)