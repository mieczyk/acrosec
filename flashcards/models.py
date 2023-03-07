from django.db import models

class Flashcard(models.Model):
    question = models.CharField(max_length=512)
    answer = models.CharField(max_length=1024)
    description = models.TextField
    external_resources = models.CharField(max_length=1024)