from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from .models import Diagnosis, Category
from .serializers import DiagnosisListSerializer, CategoryListSerializer


# Create your views here.

class DiagnosisListAPIView(ListCreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisListSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            category_db = Diagnosis.objects.get(
                code=request.data.get('code')).category.id
            diagnosis_code = Diagnosis.objects.get(
                code=request.data.get('code')).code
            if category_db == request.data.get('category') and diagnosis_code == request.data.get('code'):
                return Response({'error': 'Diagnosis already exists, kindly update!'}, status=status.HTTP_400_BAD_REQUEST)
        except:

            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class DiagnosisListAPIView2(GenericAPIView):
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
