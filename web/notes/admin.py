from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Level, Chapter, Note


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['get_name_display', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'order']
    list_filter = ['level']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Note)
class NoteAdmin(MarkdownxModelAdmin):
    list_display = ['title', 'chapter', 'is_published', 'created_at']
    list_filter = ['is_published', 'chapter__level']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']