from django.contrib import admin
from .models import Category, Diagnosis, ICD_File


admin.site.register(Category)
admin.site.register(Diagnosis)
admin.site.register(ICD_File)
