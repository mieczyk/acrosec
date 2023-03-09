import random

from django.shortcuts import render, get_object_or_404

from .models import Flashcard

def index(request):
    flashcards = list(Flashcard.objects.all())
    single_flashcard = random.choice(flashcards);
    return render(
        request, 
        'flashcards/index.html', 
        {'flashcard': single_flashcard}
    )

def check_answer(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, pk=flashcard_id)
    if request.method == 'POST':
        print(request.POST['answer'])
    return render(
        request, 
        'flashcards/index.html',
        {'flashcard': flashcard}
    )