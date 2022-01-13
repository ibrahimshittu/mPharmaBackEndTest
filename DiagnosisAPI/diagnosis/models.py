from django.db import models

# Create your models here.


class Category(models.Model):
    code = models.CharField(max_length=16, null=False, unique=True)
    title = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['code']

    def __str__(self) -> str:
        return self.title


class Diagnosis(models.Model):

    ICD_TYPES = [
        ('ICD_8a', 'ICD_8a'),
        ('ICD_9', 'ICD_9'),
        ('ICD-9-CM', 'ICD-9-CM'),
        ('ICD_10', 'ICD_10'),
        ('ICD_11', 'ICD_11'),
    ]

    code = models.CharField(max_length=16, null=False,
                            blank=False, unique=True)
    description = models.TextField(max_length=1024, null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    code_type = models.CharField(
        choices=ICD_TYPES, default='ICD_10', max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _get_full_code(self):
        "Returns the full code."
        return '%s%s' % (self.category.code, self.code)
    full_code = property(_get_full_code)
