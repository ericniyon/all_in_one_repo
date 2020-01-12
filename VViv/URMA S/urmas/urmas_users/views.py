from django.shortcuts import render, redirect
from urmas_users.models import User
from django.contrib import messages
from .forms import RegistrationForm
from django.views.generic.edit import CreateView
# Create your views here.
def login(request):
    context={}
    template_name='account/login.html'
    return render(request, template_name, context)

# class addingStaff(CreateView):
#     model = User
#     template_name = 'new_staff.html'
#     fields = [
#         'first_name',
#         'last_name',
#         'email',
#         'username',
#         'password',
#         'profile_img',
#         'is_requester',
#         'is_human_resource',
#         'is_superviser',
#         'is_autoriser',

#     ]


    # return redirect('/')
    # return render(request, template_name, context)
def AddStaff(request):
    if request.method =='POST':
        addingStaff = RegistrationForm(request.POST , request.FILES)

        if addingStaff.is_valid():
            addingStaff.save()
            messages.success(request, "New Staff has been created sussfully", extra_tags='alert')
        

    else:
        addingStaff=RegistrationForm()

        # messages.error(request, "couldn't perform such operations {}".format)
        

    template_name  =  'account/signup.html'
    context = {
        'addingStaff':addingStaff
        }
    return render(request, template_name, context)