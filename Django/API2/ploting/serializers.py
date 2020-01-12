from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Poll, Vote, Choice

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields=[
            'choice',
            'poll',
            'voted_by'
        ]

class ChoiceSerializer(serializers.ModelSerializer):

    # votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Choice
        fields= [
            'poll',
            'choice_text'
        ]


class PollsSerializer(serializers.ModelSerializer):

    # choice = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model= Poll
        fields= [
            'id',
            'question',
            'ceated_by',
            'pub_date'
        ]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username',
            'email',
            'password'
            ]

        extra_kwargs={"password":{'write_only':True}}


    def create(self, validated_data):
        user=User(
            email=validated_data['email'],
            username=validated_data['username']

        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
