from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'type': 'text', 'name': 'Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'type': 'tel', 'name': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'type': 'email', 'name': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Message', 'name': 'message'}),
        }

        labels = {
            'name': 'Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'message': 'Message',
        }

        help_texts = {
            'phone': 'Phone number must be entered in the format: +999999999. Up to 15 digits allowed.',
        }

        error_messages = {
            'name': {
                'required': 'Please enter your name.'
            },
            'phone': {
                'required': 'Please enter your phone number.'
            },
            'email': {
                'required': 'Please enter your email address.'
            },
            'message': {
                'required': 'Please enter your message.'
            }
        }