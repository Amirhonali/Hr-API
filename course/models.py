from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    keyboards = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title
