from django import forms
from django.forms import widgets



class TaskForm(forms.Form):
    description = forms.CharField(max_length=3000, required=True, label='Description', widget=widgets.Textarea(attrs={"cols": 30, "rows": 3}))
    status = forms.CharField(max_length=60, required=True, label='Status')
    created_at = forms.CharField(max_length=50, required=True, label='Created_at')
