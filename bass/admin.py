from django.contrib import admin
from .models import Bass
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Bass)
class AppNameAdmin(SummernoteModelAdmin):

    summernote_fields = ('blurb',)