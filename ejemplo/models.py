from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=200)
    done = models.BooleanField()
    deleted = models.BooleanField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)





