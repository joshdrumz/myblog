from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
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


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)
