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

    # Get previous and next notes in the same chapter
    chapter_notes = list(note.chapter.notes.filter(is_published=True).order_by('order', 'created_at'))
    current_index = next((i for i, n in enumerate(chapter_notes) if n.pk == note.pk), None)
    prev_note = chapter_notes[current_index - 1] if current_index and current_index > 0 else None
    next_note = chapter_notes[current_index + 1] if current_index is not None and current_index < len(chapter_notes) - 1 else None

    context = {
        'note': note,
        'content_html': content_html,
        'questions': questions,
        'prev_note': prev_note,
        'next_note': next_note,
        'is_blocked': False
    }

    if request.user.is_authenticated:
        return render(request, 'notes/note_detail.html', context)

    viewed_note = request.session.get('free_note_slug')

    if viewed_note is None:
        request.session['free_note_slug'] = slug
        context['is_blocked'] = False
    elif viewed_note == slug:
        context['is_blocked'] = False
    else:
        context['is_blocked'] = True

    return render(request, 'notes/note_detail.html', context)