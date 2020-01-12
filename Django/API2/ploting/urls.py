from django.urls import path, include
from ploting.views import chart_data
from .views import polls_list,polls_details
from .apiview import PollsView, PollsViewDetails, ChoicesList, CreateVote, ApiUsersView, LoginApiUser

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Polls API')


from ploting import views

urlpatterns = [
    path('sending/', views.mail, 'nano'),
    path('users/', ApiUsersView.as_view(), name='user'),
    path('', views.FFirstTemplate, name='home' ),
    path('report_builder/', include('report_builder.urls') ),
    # path('json-example/', views.json_example, name='json_example'),
    # path('json-example/data/', views.chart_data, name='chart_data'),
    path('login/', LoginApiUser.as_view(), name='user'),
    path('swagger-docs/', schema_view),
    path('polls/', PollsView.as_view()  , name='polls-list'),
    path('polls/<int:pk>/choices/', ChoicesList.as_view() , name='polls-details'),
    # path('choices/', ChoicesList.as_view(), name='choice' ),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='vote'),
    
]



