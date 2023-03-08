from django.db import models

class Flashcard(models.Model):
    question = models.CharField(max_length=512, unique=True)
    answer = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    external_resources = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.question