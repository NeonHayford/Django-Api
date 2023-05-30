from typing import Iterable, Optional
from django.db import models

# Create your models here.
class project(models.Model):
    employee = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=200)
    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length=50)

    def save(self, *args, **Kwargs):
        self.employee= f'{self.first_name} {self.last_name}'
        return super(project, self).save(*args, **Kwargs)

