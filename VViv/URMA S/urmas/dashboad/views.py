from django.shortcuts import render, redirect ,get_object_or_404
from django.template import RequestContext
# from django.contrib.auth.models import User

from urmas_users.models import User
# from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import RequestMission,RequestStaff,ReportForm, AssigneschoolForm
from .models import (
    Mission,
    Staff,
    Department,
    SchoolModel,
    Report
)
from django.contrib import messages
from django.views.generic.edit import CreateView,UpdateView
from .models import Category,Department, TransportMean, Role
from easy_pdf.views import PDFTemplateView
from django.contrib.auth.decorators import login_required, user_passes_test



# Create your views for  request model form.

def RequesterView(request):
    notification = Staff.objects.filter(requester=request.user, status='Pending').count()
    
    if request.user.is_authenticated:
        form1=RequestStaff(request.POST , request.FILES or None)
        form2=RequestMission(request.POST or None)
    
        if form1.is_valid() and form2.is_valid():


            form1.save()
            form2.save()
            form_user=form1.save()
            form_user.requester=request.user
        
            form_user.save()
            
            # messages.success(request, 'New request has been created successfully')
            messages.success(request,  "New request has been created successfully")
        
        form1=RequestStaff()
        form2=RequestMission()

        
   
    context={
        'form1':form1,
        'form2':form2,
        'notification':notification   
    }
        # return redirect('/')   
    return render(request, 'form.html', context)
# load department that has been initialized from form.py as none
def load_departments(request):
    school_id = request.GET.get('school')
    departments = Department.objects.filter(school_id=school_id).order_by('department_title')

    return render(request, 'department_dropdown_list_options.html', {'departments': departments} )

def load_schools(request):
    category_id = request.GET.get('category')
    schools = SchoolModel.objects.filter(category_id=category_id).order_by('school_name')

    return render(request, 'department_dropdown_list_options.html', {'schools': schools})


###############################view for loading roles Based on category ###########################################
def load_role(request):
    category_id = request.GET.get('category')
    role = Role.objects.filter(category_id=category_id).order_by('role_title')

    return render(request, 'department_dropdown_list_options.html', {'roles': role})
# Create your views for  dashboad.
# @login_required
# @user_passes_test(lambda user: user.username == dashboad.user.user.id)
@login_required
def DashboadViews(request):
    notification = Staff.objects.filter(requester=request.user, status='Pending').count()
    aproved = Staff.objects.filter(requester=request.user, status='Aproved').count()
    authorized = Staff.objects.filter(requester=request.user, status='Authorized').count()
    rejected = Staff.objects.filter(requester=request.user, status='Rejected').count()

    # pending = Staff.objects.filter(requester=request.user, status='Pending').count()
    
    staff= Staff.objects.filter(requester=request.user)
    # mission=Mission.objects.all()

    context={
        'staff':staff,
        'notification':notification,
        'aproved':aproved,
        'rejected':rejected,

        'authorized':authorized
        # 'mission':mission,   
    }
    template_name='pages/requestedashboad.html'

    return render(request, template_name, context)




# Create your views for  status view.

def statusViews(request):
    notification = Staff.objects.filter(requester=request.user, status='Pending').count()
    staff= Staff.objects.filter(requester=request.user)
    mission=Mission.objects.all()


    context={
        'staff':staff,
        'mission':mission,
        'notification':notification,
        
        
    }
    template_name='pages/view_status.html'

    return render(request, template_name, context)

# assign supervisor

# def SupervisorAsignement(request):
#     template_name = 'pages/addition.html'
#     form = AsignSupervisorForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#         messages.success(request, 'operation performed successfully !')

#     form = AsignSupervisorForm()

#     context={
#         'form':form
#     }
#     return render(request, template_name, context)



# reporting views


def reportingToMissions(request):
    notification = Staff.objects.filter(requester=request.user, status='Pending').count()
    
    reporting=ReportForm(request.POST , request.FILES)
    if reporting.is_valid():
        reporting.save()

        reporting_user=reporting.save()
        reporting_user.requester = request.user
        reporting_user.save()

        
        messages.success(request, 'Your report has been submitted successfuly')
        return redirect('reported')
    context={
        'reporting':reporting,
        'notification':notification
        
    }
    template_name='pages/report.html'
    

    return  render(request, template_name, context)
    
# reported missions
def ReportedMissions(request):
    notification = Staff.objects.filter(requester=request.user, status='Pending').count()

    reports=Report.objects.filter(requester=request.user)
    context={
        'reports':reports,
        'notification':notification

    }
    template_name='pages/report.html'

    return render(request, template_name, context)
# reporiting details function
def reportDetails(request, pk):
    template_name='pages/report.html'
    reportdocs = get_object_or_404(Report, pk=pk)
    context={
        'reportdocs':reportdocs
    }
    return render(request, template_name, context)
# editing/ updating your  request function based view
def EditRequest(request, pk):
    if request.user.is_authenticated:
        template_name='form.html'
        reques= get_object_or_404(Staff, pk=pk)
        reques2=get_object_or_404(Mission,pk=pk)
        if request.method=='POST':
            form1=RequestStaff(request.POST, request.FILES, instance=reques)
            form2=RequestMission(request.POST , instance=reques2)
            try:
                if form1.is_valid() and form2.is_valid() :
                    form1.save()
                    form2.save()
                    messages.success(request, 'request  has been updated successfully', extra_tags='alert')
                    # messeges.success(request, '')
            except Exception as e:
                messages.error(request, 'there is an error during update {}'.format())

        else:
            form1=RequestStaff(instance=reques)
            form2=RequestMission(instance=reques2)

        context={
            'form1':form1,
            'form2':form2,
            'reques':reques,
            'reques2':reques2,

        }

    return render(request, template_name, context)



# deleting request
def DeleteRequest(request, pk):
    template_name='form.html'
    requ=get_object_or_404(Staff, pk=pk)
    requ1=get_object_or_404(Mission, pk=pk)
    try:
        if request.method=='POST':
            form1=RequestStaff(request.POST ,request.FILES,instance=requ)
            form2=RequestMission(request.POST , instance=requ1)

            requ.delete()
            requ1.delete()
            messages.success(request, 'request has been deleted successfully')

        else:
            form1=RequestStaff(instance=requ)
            form2=RequestMission(instance=requ1)
            messages.error(request, 'Do you want to delete this request ? {}'.format)
    except Exception as e:
        pass

    context={
        'requ':requ,
        'requ1':requ1,
        'form1':form1,
        'form2':form2,
    }

    return render(request, template_name, context)

# rendering all requests that having Pending Status
def AproveRequest(request):
    
    template_name = 'pages/aprove.html'
    # schools = User.objects.filter(school=1)
    aprove=Staff.objects.all()
    
    notification = Staff.objects.filter(requester=request.user, status='Pending').count()
    context = {
        'aprove':aprove,
        'notification':notification,
        # 'schools':schools
    }

    return render(request, template_name, context)

def InvitationLeter(request, pk):
    docs = get_object_or_404(Staff ,pk=pk)

    template_name = 'pages/invitation.html'
    context={
        'docs':docs
    }
    return render(request, template_name, context)


# request details views
def RequestDetails(request, pk):

    objects = get_object_or_404(Staff , pk=pk)
    objects1 = get_object_or_404(Mission , pk=pk)

    template_name = 'pages/staff_detail.html'
    context = {
        'objects': objects,
        'objects1': objects1
    }
    return render_to_response(template_name, context)


# class PdfTest(PDFTemplateView):
#     template_name = 'pages/pdftest.html'

#     def get_context_data(self, pk):
#         template_name = 'pages/pdftest.html'
#         objects = get_object_or_404(Staff , pk=pk)

#         # send = Staff.objects.all()


#         context = {
#             'objects':objects,
#         }

#         return context
# create new user using class based view
# class NewStaffCreation(CreateView):
#     model = User
class AddCategory(CreateView):
    model = Category
    template_name='pages/addition.html'
    fields=[ 
        'name',
     ]

class AddSchool(CreateView):
    model = SchoolModel
    template_name='pages/addition.html'
    fields=[ 
        'school_name',
        'category'
     ]
    
# adding department
class AddDepartment(CreateView):
    model = Department
    template_name='pages/addition.html'
    fields=[ 
        'school',
        'department_title',
     ]
    def mesaage(request):
        messages.success(request, "Department has been created successfuly")


# adding roles
class Addingarole(CreateView):
    model = Role
    template_name = 'pages/addition.html'
    fields=[
        'role_title',
        'category',
    ]


def RequestAuthorizingChanging(request, pk):

    obj = Staff.objects.all

    objects = get_object_or_404(Staff , pk=pk)
    objects1 = get_object_or_404(Mission , pk=pk)

    template_name = 'pages/staff_detail.html'
    context = {
        'objects': objects,
        'objects1': objects1,
        'obj':obj,
    }
    Staff.objects.filter(pk=pk).update(status='Authorized')
    return render_to_response(template_name, context)


# approving request
def RequestStatusChanging(request, pk):

    obj = Staff.objects.all

    objects = get_object_or_404(Staff , pk=pk)
    objects1 = get_object_or_404(Mission , pk=pk)

    template_name = 'pages/staff_detail.html'
    context = {
        'objects': objects,
        'objects1': objects1,
        'obj':obj,
    }
    Staff.objects.filter(pk=pk).update(status='Aproved')
    return redirect('mydashboad')
 

    return render_to_response(template_name, context)

# Rejecting request

def RequestRejecting(request, pk):
    template_name = 'pages/staff_detail.html'

    objects = get_object_or_404(Staff, pk=pk)
    objects1 = get_object_or_404(Mission, pk=pk)

    context = {
        'objects':objects,
        'objects1':objects1,
    }

    Staff.objects.filter(pk=pk).update(status='Rejected')
    return render_to_response( template_name, context)

def CountingNumbers(request):
    template_name = 'base.html'
    pending = Staff.objects.filter(requester=request.user, status='Pending').count()
    context={
            
        'pending':pending,
            }

    return render(request, template_name, context)


# function used tuo updateprofile picture
class UpdatingPrifiileImage(UpdateView):
    model = User
    fields = [
        'profile_img',
    ]


# authorizer mission
def UnAuthorizedMissions(request):
    template_name = 'pages/authorixzed.html'
    authorize = Staff.objects.filter(status='Aproved')

    context = {
        'authorize':authorize,
    }
    return render(request,template_name, context)

def SchoolAssigning(request):
    template_name='pages/addition.html'
    form = AssigneschoolForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request , 'Supervisor assigned successfully')

    form = AssigneschoolForm()

    context={
        'form':form
    }

    return render(request, template_name, context)
    