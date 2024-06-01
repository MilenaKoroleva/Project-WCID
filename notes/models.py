from email.policy import default
from django.db import models

class Note(models.Model):
    titel=models.CharField(max_length=150)
    description=models.TextField(blank=True)

    class Meta:
        db_table="notes"

