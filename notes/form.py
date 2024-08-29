from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:  # Capitalized 'Meta'
        model = Notes
        fields = ['title', 'text']
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control my-5"}),
            "text": forms.Textarea(attrs={"class":"form-control mb-5"})
        }
        labels = {
            'title': "Note Title",
            'text': "Write your thoughts here",
        }
        error_messages = {
            'title': {
                'required': "Title is required.",
                'max_length': "Title is too long.",
            },
            'text': {
                'required': "Note content is required.",
            },
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError("Title must contain 'Django'")
        return title