from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import EmployeeProfile, Department, JobRole, TimeRecord

admin.site.register(EmployeeProfile)
admin.site.register(TimeRecord)
admin.site.register(Department)
admin.site.register(JobRole)
