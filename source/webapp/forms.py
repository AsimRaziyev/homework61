from django import forms
from django.forms import widgets

from webapp.models import Types, Statuses, Tag


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=50, required=True, label="Резюме:")
    description = forms.CharField(max_length=3000, required=True, label='Описание:',
                                  widget=widgets.Textarea(attrs={"cols": 30, "rows": 3}))
    status = forms.ModelChoiceField(queryset=Statuses.objects.all(), label="Статус:")
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False,
                                          widget=forms.CheckboxSelectMultiple,
                                          label="Тэг:")
    types = forms.ModelMultipleChoiceField(queryset=Types.objects.all(), required=True,
                                           widget=forms.CheckboxSelectMultiple,
                                           label="Тип:")


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='')
