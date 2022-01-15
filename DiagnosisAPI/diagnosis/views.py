from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, views
from .models import Diagnosis, Category, ICD_File
from .serializers import DiagnosisListSerializer, CategoryListSerializer, ICD_FileSerializer
from .renderer import DiagnosisRenderer

# imort parser in rest_framework
from rest_framework.parsers import FileUploadParser, MultiPartParser


# Create your views here.

class DiagnosisListAPIView(ListCreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisListSerializer
    renderer_classes = [DiagnosisRenderer]

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


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            category_db = Category.objects.get(
                code=request.data.get('code')).code
            if category_db == request.data.get('code'):
                return Response({'error': 'Category already exists, kindly update!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class DiagnosisDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisListSerializer
    lookup_field = "id"


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = "id"


class ICD_FileAPIView(views.APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file_serializer = ICD_FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
