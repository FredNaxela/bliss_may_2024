from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_control', 'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('User is not active')
        return user

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(self.request, username=username, password=password)
            if user:
                self.confirm_login_allowed(user)
            else:
                raise forms.ValidationError('Invalid login or password')

        return cleaned_data


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_control', 'placeholder': 'Password'}),
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_control',
                                                                  'placeholder': 'Confirm Password'}), label="Password")
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Full Name'}),
                           label="Full Name")
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Phone Number'}),
                            validators=[
                                RegexValidator(
                                    regex=r'^\+?1?\d{9,15}$',
                                    message="Phone number must be entered in the format: '+999999999'."
                                            " Up to 15 digits allowed."
                                )
                            ]
                            )
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'phone', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
