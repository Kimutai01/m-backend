from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from base.serializer import TeamSerializer

from rest_framework import status
from base.models import Team
from datetime import datetime

from django.utils import timezone
from pytz import timezone as tz

@api_view(['GET'])
def getTeams(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTeam(request, pk):
    team = Team.objects.get(_id=pk)
    serializer = TeamSerializer(team, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addTeam(request):
    team = Team.objects.create(
        name='Sample Name',
        logo = 'https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png',
    )
    serializer = TeamSerializer(team, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateTeam(request, pk):
    data = request.data
    team = Team.objects.get(_id=pk)
    team.name = data['name']
    team.logo = data['image']
    team.save()
    serializer = TeamSerializer(team, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteTeam(request, pk):
    team = Team.objects.get(_id=pk)
    team.delete()
    return Response('Team Deleted')

@api_view(['POST'])
@permission_classes([IsAdminUser])
def uploadImage(request):
    data = request.data
    team_id = data['team_id']
    team = Team.objects.get(_id=team_id)
    # update logo
    team.logo = request.FILES.get('image')
    team.save()

    return Response('Image was uploaded')

        
        