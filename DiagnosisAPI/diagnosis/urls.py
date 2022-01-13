from django.urls import path
from .views import DiagnosisListAPIView, DiagnosisDetailAPIView, CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path('diagnosis/', DiagnosisListAPIView.as_view(), name='diagnosis-list'),
    path('diagnosis/<int:pk>/', DiagnosisDetailAPIView.as_view(),
         name='diagnosis-detail'),
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(),
         name='category-detail'),
]
