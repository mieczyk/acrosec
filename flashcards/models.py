import re

from typing import List
from django.db import models

class Flashcard(models.Model):
    question = models.CharField(max_length=512, unique=True)
    answer = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    external_resources = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.question
    
    def is_answer_correct(self, given_answer: str) -> bool:
        if not self.answer:
            raise ModelNotInitializedError('Flashcard model must be initialized. Please fetch data from DB first.')

        if not given_answer:
            return False

        return self.__normalize_answer(self.answer) == self.__normalize_answer(given_answer)
    
    def __normalize_answer(self, answer: str) -> List[str]:
        conjunctions = ['and']
        answer = answer.lower()
        return [word for word in re.split(r'[\s\W]+', answer) if word not in conjunctions]
    
class ModelNotInitializedError(Exception):
    pass