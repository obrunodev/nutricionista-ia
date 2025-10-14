from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Patient
from .forms import PatientForm


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = 'patients'

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    context_object_name = 'patient'

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('patients:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('patients:list')

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    context_object_name = 'patient'
    success_url = reverse_lazy('patients:list')
