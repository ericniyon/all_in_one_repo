from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# from urmas_users.models import User
from django.urls import reverse


class Category(models.Model):
    name        =       models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('department')


class SchoolModel(models.Model):
    school_name         =       models.CharField(max_length=100, unique=True)
    category            =       models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.school_name

    def get_absolute_url(self):
       
        return reverse('mydashboad')


class Department(models.Model):
    school                  =       models.ForeignKey(SchoolModel, on_delete=models.CASCADE, null=True)
    department_title        =       models.CharField(max_length=250, unique=True)
    
    

    def __str__(self):
        return self.department_title


    def get_absolute_url(self):
        return reverse('mydashboad')



# MEANS=(
#     (0, "--------"),
#     (1, "Provided"),
#     (2, "Personal"),
#     (3, "Public")
# )
class TransportMean(models.Model):
    tansport_mean = models.CharField(max_length=20, blank=True,unique=False)

    def __str__(self):
        return self.tansport_mean

class Role(models.Model):
    role_title          =       models.CharField(max_length=100)
    category            =       models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.role_title

    def get_absolute_url(self):
        return reverse('mydashboad')







STATUS=(
    ('Aproved', 'Aproved'),
    ('Rejected', 'Rejected'),
    ('Pending', 'Pending'),
    ('Authorized', 'Authorized'),
)

class Staff(models.Model):

    requester           =       models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    school              =       models.ForeignKey(SchoolModel, on_delete=models.CASCADE, null=True, blank=True)
    staff_id            =       models.CharField(max_length=20,help_text='Eg- 123,12A etc',null=True, blank=True)
    name                =       models.CharField(max_length=100)
    phone_number        =       models.IntegerField(null=True, blank=True)
    email               =       models.EmailField(help_text='Eg- example@gmail.com')
    category            =       models.ForeignKey(Category, on_delete=models.CASCADE)
    department          =       models.ForeignKey(Department, on_delete=models.CASCADE)
    role                =       models.ForeignKey(Role, on_delete=models.CASCADE)  
    transport           =       models.ForeignKey(TransportMean,on_delete=models.CASCADE,blank=True, null=True)
    upload_file         =       models.FileField(upload_to='request_doc',null=True, blank=True,help_text='upload your invitstion latter') 
    status              =       models.CharField(max_length=50, choices=STATUS, default='Pending') 
    requested_on        =       models.DateTimeField(auto_now_add=True,null=True,)
        
    # def opening_uploaded_file(self):
    #     # with open(self.upload_file.path) as file:
    #     #     return file.read().replace('\n','<br>')
    #     with open(self.upload_file.path) as fileobj:
    #         for row in fileobj:
    #             return fileobj.replace('\n','<br>')





class Mission(models.Model):
    staff_issued_to     =       models.ManyToManyField(Staff)
    purpose             =       models.CharField(max_length=200,help_text='mission purpose')
    result              =       models.CharField(max_length=200, help_text='expected result to your mission')
    destnation          =       models.CharField(max_length=100, help_text='address')
    distance            =       models.CharField(max_length=40,help_text='Eg- 4km')
    dipature_date       =       models.DateField(help_text='Eg- YY-MM-DD')
    returnning_date     =       models.DateField(help_text='Eg- YY-MM-DD')
    duration_of_mission =       models.CharField(max_length=100,help_text='Eg- 10 days and 10 nights')
    invitation_latter   =       models.FileField(null=True, blank=True)
    


class Report(models.Model):
    file            =       models.FileField(help_text='Upload .pdf file')
    note            =       models.TextField(null=True, blank=True)
    requester           =       models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('report')

    
    

STATUS=(
    (0, "Pendding"),
    (1, "Approved"),
    (2, 'Rejected'),
    (3, 'Authorised'),
)
class SchoolSupervisor(models.Model):
    supervisor          =       models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    school              =           models.ForeignKey( SchoolModel, null=True, blank=True, on_delete=models.SET_NULL)  
    

    def __str__(self):
        return self.school
    





    
    
    
        
    