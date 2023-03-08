import random

from django.shortcuts import render

from .models import Flashcard


def index(request):
    flashcards = list(Flashcard.objects.all())
    single_flashcard = random.choice(flashcards);
    return render(
        request, 
        'flashcards/index.html', 
        {'flashcard': single_flashcard}
    )