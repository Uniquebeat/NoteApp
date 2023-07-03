from .models import NoteModel
from django.forms import ModelForm, Textarea, TextInput


class NoteForm(ModelForm):
    class Meta:
        model = NoteModel
        fields = ['title', 'body']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Input Title Here'
            }),
            'body': Textarea(attrs={
                'placeholder': 'Input Body Here'
            })
        }