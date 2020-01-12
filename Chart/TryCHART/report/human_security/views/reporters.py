from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from human_security.forms import MemberSignupForm
from human_security.models import User, Result


class MemberSignUpView(CreateView):
    model = User
    form_class = MemberSignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class ResultListView(ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'human_security/result_list.html'

    def get_queryset(self):

        reporter = self.request.user.reporter
        member_location = reporter.location.values_list('pk', flat=True)
        queryset = Result.objects.filter(location__in=member_location)\


        return queryset
