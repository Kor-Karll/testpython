from django import forms

class PostSearchFrom(forms.Form):
    search_word = forms.CharField(label='Search Word')