from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


class RegisterDoctorForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    username = forms.EmailField(
        max_length=254, help_text='Enter a valid email address', label="Email")
    isDoctor = forms.BooleanField(
        widget=forms.HiddenInput(), initial=True, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'specialization',
            'isDoctor',
        ]


class RegisterPatientForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    username = forms.EmailField(
        max_length=254, help_text='Enter a valid email address', label="Email")
    isDoctor = forms.BooleanField(
        widget=forms.HiddenInput(), initial=False, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'age',
            'disease',
            'allergies',
            'isDoctor',
        ]

class LoginFormDoctor(forms.Form):
    username = forms.EmailField(max_length=255, required=True,label="Email")
    password = forms.CharField(widget=forms.PasswordInput, required=True,label="Password")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.add_message(request, messages.ERROR, "Invalid Credentials")
            return -1
        if User.objects.get(username=username).isDoctor:
            user = authenticate(username=username, password=password)
            return user
        else:
            messages.add_message(request, messages.ERROR, "You are not registered as a Doctor")
            return -1

class LoginFormPatient(forms.Form):
    username = forms.EmailField(max_length=255, required=True,label="Email")
    password = forms.CharField(widget=forms.PasswordInput, required=True,label="Password")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.add_message(request, messages.ERROR, "Invalid Credentials")
            return -1
        if not User.objects.get(username=username).isDoctor:
            user = authenticate(username=username, password=password)
            return user
        else:
            messages.add_message(request, messages.ERROR, "You are not registered as a Patient")
            return -1