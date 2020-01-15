from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory, Comment
from django.db import models
# from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Title/date', {'fields': ['title', 'description', 'published']}),
        ('URL', {'fields': ['slug']}),
        ('Series', {'fields': ['series']}),
        ('Content', {'fields': ['content']})
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget()}
    }


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'tutorial', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Comment, CommentAdmin)
