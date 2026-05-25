from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import markdown as md
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

    # Convert markdown to HTML
    content_html = mark_safe(md.markdown(
        note.content,
        extensions=['extra', 'codehilite', 'toc']
    ))

    if request.user.is_authenticated:
        return render(request, 'notes/note_detail.html', {
            'note': note,
            'content_html': content_html,
            'questions': questions,
            'is_blocked': False
        })

    viewed_note = request.session.get('free_note_slug')

    if viewed_note is None:
        request.session['free_note_slug'] = slug
        is_blocked = False
    elif viewed_note == slug:
        is_blocked = False
    else:
        is_blocked = True

    return render(request, 'notes/note_detail.html', {
        'note': note,
        'content_html': content_html,
        'questions': questions,
        'is_blocked': is_blocked
    })