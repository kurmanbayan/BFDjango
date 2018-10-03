from django.db import models
import datetime

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=120)
    createdAt = models.DateField(default=datetime.date.today)
    dueTo = models.DateField()
    owner = models.CharField(max_length=50)c
    mark = models.BooleanField(default=False)

    def __str__(self):
        return self.todo
