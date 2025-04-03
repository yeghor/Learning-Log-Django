from django import forms
from .models import Topics, Entry

class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['text']
        labels = {'text': 'Name'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
        labels = {'title': 'Title:', 'text': 'Text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
