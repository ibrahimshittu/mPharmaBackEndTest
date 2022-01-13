from rest_framework import serializers
from .models import Diagnosis, Category


class DiagnosisListSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=16)
    description = serializers.CharField()
    code_type = serializers.CharField(max_length=16)

    class Meta:
        model = Diagnosis
        fields = ['code', 'description', 'code_type']


class CategoryListSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=16)
    title = serializers.CharField()

    class Meta:
        model = Category
        fields = ['code', 'title']
