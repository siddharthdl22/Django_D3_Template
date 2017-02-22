from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    grade = models.IntegerField()
