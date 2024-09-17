from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from base.serializer import FixtureSerializer

from rest_framework import status
from base.models import Fixture
from datetime import datetime

from django.utils import timezone
from pytz import timezone as tz

@api_view(['GET'])
def getFixtures(request):
    fixtures = Fixture.objects.all()
    serializer = FixtureSerializer(fixtures, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFixture(request, pk):
    fixture = Fixture.objects.get(_id=pk)
    serializer = FixtureSerializer(fixture, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addFixture(request):
    fixture = Fixture.objects.create(
        team1='Sample Team 1',
        team2='Sample Team 2',
        
        date='2021-01-01',
        time = '00:00:00',
        category='Sample Category',
        stadium='Sample Stadium',
        
    )
    serializer = FixtureSerializer(fixture, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateFixture(request, pk):
    data = request.data
    fixture = Fixture.objects.get(_id=pk)
    fixture.team1 = data['team1']
    fixture.team2 = data['team2']
    fixture.date = data['date']
    fixture.time = data['time']
    fixture.category = data['category']
    fixture.stadium = data['stadium']
    fixture.save()
    serializer = FixtureSerializer(fixture, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteFixture(request, pk):
    fixture = Fixture.objects.get(_id=pk)
    fixture.delete()
    return Response('Fixture was deleted')

@api_view(['POST'])
def uploadImage(request):
    data = request.data
    fixture_id = data['fixture_id']
    fixture = Fixture.objects.get(_id=fixture_id)

    fixture.image = request.FILES.get('image')
    fixture.save()

    return Response('Image was uploaded')
