from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Diagnosis, Category
from .serializers import DiagnosisListSerializer, CategoryListSerializer


# Create your views here.

class DiagnosisListAPIView(ListCreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisListSerializer


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class DiagnosisDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisListSerializer
    lookup_field = 'id'


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'
