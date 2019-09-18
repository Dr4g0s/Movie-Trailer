from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name' : forms.TextInput(attrs={"name":"name", "id":"name"}),
            'email' : forms.TextInput(attrs={"name":"email", "id":"email"}),
            'message' : forms.Textarea(attrs={"name":"message", "id":"message"}),
        }
