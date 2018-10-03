from django.db import models
import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=300)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    created_at = models.DateField(default=datetime.date.today)
    blog_fk = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
