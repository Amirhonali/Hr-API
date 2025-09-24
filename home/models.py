from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    keyboards = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)


    def __str__(self):
        return self.title
