from django import forms
from urmas_users.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields=[
            'first_name',
            'last_name',
            'email',
            'school',
            'username',
            'password1',
            'password2',
            'is_requester',
            'is_human_resource',
            'is_superviser',
            'is_autoriser',
            
        ]
        # widgets = {
        #  'username': forms.TextInput(attrs={'class': 'form-control-sm has-success'}),
        #  'first_name': forms.TextInput(attrs={'class': 'form-control-sm'}),
        #  'last_name': forms.TextInput(attrs={'class': 'form-control-sm form-control-sm'}),
        #  'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
        #  'password1': forms.PasswordInput(attrs={'class': 'form-control-sm form-control-sm'}),
        #  'password2': forms.PasswordInput(attrs={'class': 'form-control-sm form-control-sm'}),
        #  'school': forms.PasswordInput(attrs={'class': 'form-control-sm form-control-sm'}),



        #  }
        # widgets = {
        # 'first_name': forms.CharField(attrs={'class': 'form-control-sm form-control-sm'}),
        # 'last_name': forms.CharField(attrs={'class': 'form-control-sm form-control-sm'}),
        # 'email': forms.EmailField(attrs={'class': 'form-control-sm form-control-sm'}),
        # 'school': forms.CharField(attrs={'class': 'form-control-sm form-control-sm'}),
        # 'username': forms.CharField(attrs={'class': 'form-control-sm form-control-sm'}),
        # 'password1': forms.PasswordInput(attrs={'class': 'form-control-sm form-control-sm'}),
        # 'password2': forms.PasswordInput(attrs={'class': 'form-control-sm form-control-sm'}),


    # }
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

