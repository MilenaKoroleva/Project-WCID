from email.policy import default
from django.db import models

class Task(models.Model):
    titel=models.CharField(max_length=150)
    important=models.BooleanField(default=False)
    urgently=models.BooleanField(default=False)
    todo_date=models.DateField(blank=True, null=True)
    description=models.TextField(blank=True)

    class Meta:
        db_table="task_list"

