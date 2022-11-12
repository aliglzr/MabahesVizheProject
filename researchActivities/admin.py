from django.contrib import admin
from researchActivities.models import Paper
from researchActivities.models import Journal
from researchActivities.models import Conference


class PaperAdmin(admin.ModelAdmin):
    list_display = (
    "title", "doi", "author1", "author2", "author3", "author4", "publication_date", "conference", "journal", "paper_image")


class ConferenceAdmin(admin.ModelAdmin):
    list_display = ("confTopic", "title", "confType", "event_date", "event_place")


class JournalAdmin(admin.ModelAdmin):
    list_display = ("journalType", "title", "issn", "volume", "publisher", "rank")


admin.site.register(Paper, PaperAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Conference, ConferenceAdmin)

# Register your models here.
