from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname")

admin.site.register(Patient, PatientAdmin)