from django import forms
from .models import Contact, Session


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Your name'}),
            'phone': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Message', 'name': 'message',
                                             'style': 'height: 240px'}),
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


class SessionForm(forms.ModelForm):
    MASSAGE_SPA_CHOICES = [
        ('massage', 'Massage'),
        ('spa', 'Spa'),
        ('massage+spa', 'Massage & Spa')
    ]

    procedure = forms.ChoiceField(
        choices=MASSAGE_SPA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Select Procedure'}),
    )

    class Meta:
        model = Session
        fields = ['name', 'phone', 'email', 'message', 'date', 'time', 'procedure']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Phone Number'}),
            'time': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Time format: hh:mm'}),
            'date': forms.TextInput(attrs={'class': 'form_control', 'id': 'my_date_picker',
                                           'placeholder': 'Select Date'}),
            'message': forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Message(optional)'}),
        }

        labels = {
            'name': 'Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'procedure': 'Procedure',
            'date': 'Date',
            'time': 'Time',
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
            'procedure': {
                'required': 'Please enter your procedure.'
            },
            'date': {
                'required': 'Please enter your date.'
            },
            'time': {
                'required': 'Please enter your time.'
            }
         }
