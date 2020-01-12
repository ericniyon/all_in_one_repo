from django.http import HttpResponse
from django.shortcuts import render


def home_page_view(request):
    page_title = 'SYC'
    return render(request, 'home_page.html', {'title': page_title})



def about_page_view(request):
    return render(request, 'home_page.html', {'title': "ABOUT PAGE"})
    



def contact_page_view(request):
    return render(request, 'home_page.html', {'title': "CONTACT PAGE"})
    