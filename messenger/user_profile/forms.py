from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    """
    Форма модели Chat, которая позволяет создать новый чат
    """
    # member = forms.
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'avatar')
