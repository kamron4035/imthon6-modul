from django import forms
from .models import Tudo


class TudoForm(forms.ModelForm):
    class Meta:
        model = Tudo
        fields = [
            "user",
            "title",
            "content",
        ]

