from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from .models import Poll,Choice
import requests

from django.core.mail import send_mail

from django.conf import settings
from django.http import HttpResponse


def mail(request):
     send_mail(
        'email remainder for report', 
        'Hey! you have not send report for last week please submeet your report inorder to help others to kwnow what is going on', 
        'niyoeri6@gmail.com',
         ['niyoeri6@gmail.com'])

    return render(request, 'home.html')

# def home(request):
#     response = requests.get('http://api.ipstack.com/154.68.126.68?access_key=69170dda95a9cf87511d38db0a0ac61a')
#     geodata = response.json()
#     return render(request, 'home.html', {
#         'country_name': geodata['country_name'],
#         # 'id': geodata['id']
#     })

def chart_data(request):
    dataset = Choice.objects \
        .values('choice_text') \
        .exclude(choice_text='') \
        .annotate(total=Count('choice_text')) \
        .order_by('choice_text')

    port_display_name = dict()
    for port_tuple in Choice:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic'},
        'labels':{'one':'nana'},
        'series': [{
            'name': 'Embarkation ',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)




def polls_list(request):
    MAX_OBJECTS=20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data={"results":list(polls.values("question","ceated_by__username","pub_date"))}
    return JsonResponse(data)





def polls_details(request, pk):
    poll = get_list_or_404(Poll, pk=pk)
    data={"results": {
        "question":poll.question,
        "ceated_by":poll.ceated_by.username,
        "pub_date":poll.pub_date,
    }}
    return JsonResponse(data)

def FFirstTemplate(request):
    myName={'name':'Madiba'}
    return render (request, 'home.html', myName)