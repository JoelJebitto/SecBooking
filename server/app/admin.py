# Register your models here.
from django.contrib import admin
from .models import Class, Exam, AnswerSheet, Profile

admin.site.register(Class)
admin.site.register(Exam)
admin.site.register(AnswerSheet)
admin.site.register(Profile)