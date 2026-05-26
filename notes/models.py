from django.db import models
from markdownx.models import MarkdownxField


class Level(models.Model):
    LEVEL_CHOICES = [
        ('SC', 'SC Computer Science'),
        ('HSC', 'HSC Computer Science'),
        ('BSC', 'BSc Computer Science'),
    ]

    name = models.CharField(max_length=10, choices=LEVEL_CHOICES, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.get_name_display()


class Chapter(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='chapters')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.level} — {self.name}"


class Note(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    content = MarkdownxField()
    summary = models.TextField(blank=True, help_text="Short summary shown on the notes list page")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title