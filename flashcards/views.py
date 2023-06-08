import random

from django.shortcuts import render, redirect, get_object_or_404

from .models import Flashcard

def welcome(request):
    return render(request, "flashcards/welcome.html")

def home(request):
    if request.method == 'POST':
        request.session['nickname'] = request.POST.get('nickname')
        return redirect('/start')
    return render(request, 'flashcards/home.html')

def start(request):
    flashcards = list(Flashcard.objects.all())
    single_flashcard = random.choice(flashcards);
    return render(
        request, 
        'flashcards/start.html', 
        {'flashcard': single_flashcard, 'nickname': request.session['nickname']}
    )

def check_answer(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, pk=flashcard_id)
    
    is_answer_correct = False
    answered = False
    if request.method == 'POST':
        answered = True
        is_answer_correct = flashcard.is_answer_correct(request.POST['answer'])    

    return render(
        request, 
        'flashcards/start.html',
        {
            'flashcard': flashcard,
            'answered': answered,
            'is_answer_correct': is_answer_correct
        }
    )