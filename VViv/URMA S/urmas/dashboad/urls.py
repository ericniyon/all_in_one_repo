"""urmas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from dashboad import views as dashboad_views

urlpatterns = [
    path('account/', include('allauth.urls')),
    path('auto/<int:pk>/', dashboad_views.RequestRejecting, name='reject'),
    path('request/', dashboad_views.RequesterView, name='requesting'),
    path('updete/<int:pk>/', dashboad_views.EditRequest, name='update'),
    path('delete/<int:pk>/', dashboad_views.DeleteRequest, name='delete'),
    path('aprove/', dashboad_views.AproveRequest, name='aprove'),
    path('details/<int:pk>/', dashboad_views.RequestDetails, name='details'),
    # pdf test url
    path('aprove/<int:pk>/', dashboad_views.RequestStatusChanging, name='task'),
    path('authorized/<int:pk>/', dashboad_views.RequestAuthorizingChanging, name='autho'),
    # adding category
    path('category/', dashboad_views.AddCategory.as_view(), name='category'),
    # adding department
    path('department/', dashboad_views.AddDepartment.as_view(), name='department'),
    # adding school
    path('school/', dashboad_views.AddSchool.as_view(), name='school'),
    # add role
    # invitation
    path('invitation/later/<int:pk>/', dashboad_views.InvitationLeter, name='invitation'),
    path('role/', dashboad_views.Addingarole.as_view(), name='role'),

    # assign school to supervisor
    path('assign/supervisor/', dashboad_views.SchoolAssigning, name='assigning'),

    # authorixer page
    path('aproved/', dashboad_views.UnAuthorizedMissions, name='authorized'),

    # reported mission
    path('reported/',dashboad_views.ReportedMissions, name='reported'),
    # report detail url
    path('report/view/<int:pk>', dashboad_views.reportDetails, name='details_repo'),
    path('', dashboad_views.DashboadViews, name='mydashboad'),
    # suervizor assignment

    # path('assign/supervizor', dashboad_views.SupervisorAsignement, name='supervizor'),
    path('image/<int:pk>/', dashboad_views.UpdatingPrifiileImage.as_view(), name='img'),
    path('status/',dashboad_views.statusViews, name='viewstatus'),
    path('roport/', dashboad_views.reportingToMissions, name='report'),
    path('ajax/load-departments/', dashboad_views.load_departments, name='ajax_load_departments'),
    
    path('ajax/load-schools/', dashboad_views.load_schools, name='ajax_load_schools'),
   
    path('ajax/load-roles/', dashboad_views.load_role, name='ajax_load_roles'),
    
]
