from django.shortcuts import render
from rest_framework import generics
from studentapi.models import Student
from studentapi.serializers import StudentSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
