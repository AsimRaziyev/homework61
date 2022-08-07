from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def clean(self):
        if not self.cleaned_data.get("first_name") and not self.cleaned_data.get("last_name"):
            raise ValidationError("Заполните одно из этих полей 'First name', 'Last name'")
        return super().clean()
