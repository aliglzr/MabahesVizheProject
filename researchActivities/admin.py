from django.contrib import admin
from researchActivities.models import Paper
from researchActivities.models import Journal
from researchActivities.models import Conference

admin.site.register(Paper)
admin.site.register(Journal)
admin.site.register(Conference)

# Register your models here.
