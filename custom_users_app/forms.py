from django import forms
# Learned about this from Kevin Blount
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from custom_users_app.models import CustomUser

# Create your forms here.
class AddLoginForm(forms.Form):
    # Got help here from Kevin Blount, Sohail Aslam in study hall.
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

class AddSignupForm(forms.ModelForm):
    # Got help here from Kevin Blount, Sohail Aslam in study hall.
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['displayname']
