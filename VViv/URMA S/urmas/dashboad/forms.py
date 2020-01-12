from django import forms

from django.contrib.auth import get_user_model
from .models import Staff, Mission,SchoolSupervisor,Department,Report, SchoolModel, Role





class RequestStaff(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            # 'staff_id',
            'name',
            'category',
            'school',
            'department',
            'role',
            'transport',
            'upload_file'   
        ]
        widgets = {
         'upload_file': forms.FileInput(attrs={'style': 'border:2px solid #AAA; border-radius:4px;padding:2px 5px;margin:2px;background:#DDD;display:inline-block;outline:none;position:relative;overflow: hidden; background: -webkit-linear-gradient(top, #f9f9f9, #e3e3e3);'}),
        }
        
    
    #################################load schools based on category ###################################################

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['school'].queryset = SchoolModel.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['school'].queryset = SchoolModel.objects.filter(category_id=category_id).order_by('school_name')

            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['school'].querset = self.instance.category.school_set.order_by('school_name')
    
        # initialize depertiment field to none in selection field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['department'].queryset = Department.objects.none()

        if 'school' in self.data:
            try:
                school_id = int(self.data.get('school'))
                self.fields['department'].queryset = Department.objects.filter(school_id=school_id).order_by('department_title')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty 
        elif self.instance.pk:
            self.fields['department'].queryset = self.instance.school.department_set.order_by('department_title')

    #################################load Roles based on category ###################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['role'].queryset = Role.objects.filter(category_id=category_id).order_by('role_title')

            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['role'].querset = self.instance.category.role_set.order_by('role_title')

# mission request model form
class RequestMission(forms.ModelForm):
    class Meta:

        model = Mission
        fields=[
            'purpose',
            'result',
            'destnation',
            'distance',
            'dipature_date',
            'returnning_date',
            'duration_of_mission',
            
        ]
    
   
    

# requesting  model form

# report model form

class ReportForm(forms.ModelForm):

    
    class Meta:
        model = Report
        fields = ("file","note")

# adding staff details in my system
# class StaffProfileForm(forms.ModelForm):
    
#     class Meta:
#         model = ProfileImage
#         fields = [
#             'profile'
#         ]

        
# class AsignSupervisorForm(forms.ModelForm):
    
#     class Meta:
#         model = SchoolModel
#         fields = ( "superviser")

# class AssignTo2Form(forms.ModelForm):
    
#     class Meta:
#         model = Staff
#         fields = ("school")
class AssigneschoolForm(forms.ModelForm):
    
    class Meta:
        model = SchoolSupervisor
        fields = (
            "supervisor",
            "school"
            )

