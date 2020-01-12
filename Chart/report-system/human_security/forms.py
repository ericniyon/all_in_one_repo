from django import forms
from django.contrib.auth.forms import UserCreationForm
from human_security.models import (Reporter, Location, User, Result)


class MemberSignupForm(UserCreationForm):
    location = forms.ModelMultipleChoiceField(
        queryset=Location.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_reporter = True
        user.save()
        member = Reporter.objects.create(name=user)
        member.location.add(*self.cleaned_data.get('location'))
        return user




