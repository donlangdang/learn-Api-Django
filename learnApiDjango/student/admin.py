from django.contrib import admin
from .models import Student, Subject, Student_Subject, CustomUsers

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Student_Subject)
admin.site.register(CustomUsers)