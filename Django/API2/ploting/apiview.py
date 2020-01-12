from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from .models import Poll, Choice, Vote
from rest_framework import generics
from .serializers import PollsSerializer, ChoiceSerializer, VoteSerializer,UsersSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.exceptions import PermissionDenied



class LoginApiUser(APIView):

    permission_classes=()
    
    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})

        else:
            return Response({'error': "Wrong Cresidentials"}), status==status.HTTP_400_BAD_REQUEST


# api user creations view

class ApiUsersView(generics.CreateAPIView):
    authentication_classes= ()
    permission_classes=()
    serializer_class=UsersSerializer

class PollsView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class=PollsSerializer



class PollsViewDetails(generics.RetrieveDestroyAPIView):
    queryset=Poll.objects.all()
    serializer_class=PollsSerializer


class ChoicesList(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset=Choice.objects.filter(poll_id=self.kwargs['pk'])
        
        return queryset
    
    serializer_class=ChoiceSerializer


class CreateVote(APIView):
    
    serializer_class=VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










# class PollsView(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()[:20]
#         data=PollsSerializer(polls, many=True).data
#         return Response(data)



# class PollsViewDetails(APIView):
#     def get(self, request, pk):
#         poll = get_list_or_404(Poll, pk=pk)
#         data=PollsSerializer(poll).data
#         return Response(data)