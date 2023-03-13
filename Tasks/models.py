from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_title = models.CharField(max_length=200)
    task_type = models.CharField(max_length=20)
    task_details = models.TextField()
    due_date = models.DateField(default='2000-01-01')
    time_created = models.DateTimeField(auto_now_add=True)


# this is a django model