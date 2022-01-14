from rest_framework import serializers
from .models import Diagnosis, Category


class DiagnosisListSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=16)
    description = serializers.CharField()
    full_code = serializers.SerializerMethodField()
    category_code = serializers.SerializerMethodField()
    category_title = serializers.SerializerMethodField()

    def get_full_code(self, obj):
        return obj.category.code + str(obj.code)

    def get_category_code(self, obj):
        return str(obj.category.code)

    def get_category_title(self, obj):
        return str(obj.category.title)

    class Meta:
        model = Diagnosis
        fields = ['id', 'category_code', 'code', 'full_code', 'description', 'category',
                  'category_title', 'code_type', 'created_at']


class CategoryListSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=16)
    title = serializers.CharField()

    class Meta:
        model = Category
        fields = ['id', 'code', 'title', 'created_at']
