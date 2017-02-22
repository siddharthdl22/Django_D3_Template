from rest_framework import serializers
from studentapi.models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    grade = serializers.IntegerField()
