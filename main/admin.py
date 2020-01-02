from django.contrib import admin
from .models import Tutorial
from django.db import models
from ckeditor.widgets import CKEditorWidget

# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Title/date', {'fields': ['title', 'description', 'published']}),
        ('Content', {'fields': ['content']}),
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}
    }


admin.site.register(Tutorial, TutorialAdmin)
