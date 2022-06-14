from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from django.forms.widgets import PasswordInput, TextInput

class LoginForm(forms.Form):
    # username = forms.CharField(max_length=63, label="Nom d'utilisateur", widget=forms.TextInput(attrs={'placeholder': 'Démo'}))
    # password = forms.CharField(max_length=63, label="Mot de passe", widget=forms.PasswordInput(attrs={'placeholder': 'Démoblog1'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-select'



class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_photo', )