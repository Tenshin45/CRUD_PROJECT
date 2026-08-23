from .models import Product
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your forms here.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter product price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'placeholder': 'Select product image', 'accept': 'image/*', 'capture': 'camera', 'onchange': 'previewImage(event)'}),
        }
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}))
class LogoutForm(forms.Form):
    confirm_logout = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), label='Confirm logout')