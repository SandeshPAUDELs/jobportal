from django.contrib import admin
from .models import Application, Job, SaveJob

# Register your models here.

admin.site.register(Job)
admin.site.register(Application)
admin.site.register(SaveJob)