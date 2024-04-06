from django.shortcuts import render
from rest_framework import viewsets

from teachers.models import Category, Teachers
from teachers.serializers import CategorySerializer, TeacherSerializer


# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = (
        "title",
    )


class TeacherView(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    search_fields = (
        "title",
    )
