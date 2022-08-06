from django import forms
from .models import User



class UserSignupForm(forms.ModelForm):
    class Meta:
       model = User
       fields = ['email', 'username']
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=user).exists():

            raise forms.ValidationError('username exist')

        return user

    def clean_password(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exist')

        return email

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('password not mach')

        return password1


