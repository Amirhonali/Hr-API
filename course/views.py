from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from course.models import Course
from course.serializers import CourseSerializer


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer