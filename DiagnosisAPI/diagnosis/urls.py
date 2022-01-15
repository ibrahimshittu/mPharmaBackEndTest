from django.urls import path
from .views import DiagnosisListAPIView, DiagnosisDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, ICD_FileAPIView

urlpatterns = [
    path('diagnosis/', DiagnosisListAPIView.as_view(), name='diagnosis-list'),
    path('diagnosis/<int:id>/', DiagnosisDetailAPIView.as_view(),
         name='diagnosis-detail'),
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:id>/', CategoryDetailAPIView.as_view(),
         name='category-detail'),
    path('icd_file_upload/',
         ICD_FileAPIView.as_view(), name='icd_file'),

]
