from apps.patients.models import Patient

from django.contrib import admin


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    ...
