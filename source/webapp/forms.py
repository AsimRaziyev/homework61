from django import forms
from django.forms import widgets

from webapp.models import Type, Status


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=50, required=False, label="Резюме:")
    description = forms.CharField(max_length=3000, required=True, label='Описание:',
                                  widget=widgets.Textarea(attrs={"cols": 30, "rows": 3}))
    status_text = forms.ModelChoiceField(queryset=Status.objects.all())
    type_text = forms.ModelChoiceField(queryset=Type.objects.all())