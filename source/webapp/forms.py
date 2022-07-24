import re
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["summary", "author", "description", "status", "tags", "types"]
        widgets = {
            "tags": widgets.CheckboxSelectMultiple,
            "types": widgets.CheckboxSelectMultiple,
            "description": widgets.Textarea(attrs={"placeholder": "введите текст", "cols": 30, "rows": 3})
        }

    def clean(self):
        author = self.cleaned_data.get("author")
        print(author)
        if not re.match("^[a-zA-ZА-Яа-я\s]+$", author):
            self.add_error("author", ValidationError("Вводите только буквы"))

        if self.cleaned_data.get("summary") == self.cleaned_data.get("description"):
            raise ValidationError("Название и описание не могут совпадать")
        return super().clean()


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')
