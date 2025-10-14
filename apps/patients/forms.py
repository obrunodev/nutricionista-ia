from apps.patients.models import Patient

from django import forms


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['name', 'document', 'birth_date', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'document': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'gender': forms.Select(attrs={'class': 'form-select'}),
        }
