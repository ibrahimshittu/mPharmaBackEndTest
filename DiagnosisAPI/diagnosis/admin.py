from django.contrib import admin
from .models import Category, Diagnosis, ICD_File


admin.site.register(Category)

admin.site.register(ICD_File)


class diagnosisAdmin(admin.ModelAdmin):
    list_display = ('code', 'full_code', 'description',
                    'category', 'code_type', 'created_at', 'updated_at')
    list_filter = ('category', 'code_type')
    ordering = ['code']


admin.site.register(Diagnosis, diagnosisAdmin)
