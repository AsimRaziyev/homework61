from django import forms
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def clean(self):
        # if not self.cleaned_data.get("first_name") and not self.cleaned_data.get("last_name"):
        if not (self.cleaned_data.get("first_name") or self.cleaned_data.get("last_name")):
            raise forms.ValidationError(" Необходимо указать 'First name' или 'Last name'!")
        return super().clean()
