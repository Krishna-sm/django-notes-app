from django.contrib import admin
from .models import Note
# Register your models here.

admin.site.index_title="Notes App"
admin.site.site_header="Notes App"

admin.site.register(Note)