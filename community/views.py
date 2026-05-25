from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from notes.models import Note
from .models import Question, Answer


@login_required
def question_board(request):
    questions = Question.objects.select_related('note', 'user').all()
    return render(request, 'community/question_board.html', {
        'questions': questions
    })


@login_required
def add_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        body = request.POST.get('body', '').strip()
        if body:
            Answer.objects.create(
                question=question,
                user=request.user,
                body=body
            )
            messages.success(request, 'Your answer was posted successfully.')
    return redirect('notes:note_detail', slug=question.note.slug)


@login_required
def upvote_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.upvotes += 1
    answer.save()
    return redirect('notes:note_detail', slug=answer.question.note.slug)


@login_required
def accept_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    # Only the note owner (admin) can accept answers
    if request.user.is_staff:
        # Unaccept all other answers for this question first
        Answer.objects.filter(question=answer.question).update(is_accepted=False)
        answer.is_accepted = True
        answer.save()
        # Mark question as answered
        answer.question.is_answered = True
        answer.question.save()
        messages.success(request, 'Answer marked as accepted.')
    return redirect('notes:note_detail', slug=answer.question.note.slug)