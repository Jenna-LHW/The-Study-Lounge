from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Level, Chapter, Note


def home(request):
    levels = Level.objects.all()
    return render(request, 'notes/home.html', {'levels': levels})


def level_detail(request, slug):
    level = get_object_or_404(Level, slug=slug)
    chapters = level.chapters.all()
    return render(request, 'notes/level_detail.html', {
        'level': level,
        'chapters': chapters
    })


def chapter_detail(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)
    notes = chapter.notes.filter(is_published=True)
    return render(request, 'notes/chapter_detail.html', {
        'chapter': chapter,
        'notes': notes
    })


def note_detail(request, slug):
    note = get_object_or_404(Note, slug=slug, is_published=True)
    questions = note.questions.all()

    # Logged in — full access
    if request.user.is_authenticated:
        return render(request, 'notes/note_detail.html', {
            'note': note,
            'questions': questions,
            'is_blocked': False
        })

    # Not logged in — check session
    viewed_note = request.session.get('free_note_slug')

    if viewed_note is None:
        # First note — allow and save to session
        request.session['free_note_slug'] = slug
        is_blocked = False

    elif viewed_note == slug:
        # Same note — allow again
        is_blocked = False

    else:
        # Second note — block
        is_blocked = True

    return render(request, 'notes/note_detail.html', {
        'note': note,
        'questions': questions,
        'is_blocked': is_blocked
    })