from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.models import Match

from base.serializer import MatchSerializer


@api_view(['GET'])
def getMatches(request):
    matches = Match.objects.all()
    serializer = MatchSerializer(matches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMatch(request, pk):
    match = Match.objects.get(_id=pk)
    serializer = MatchSerializer(match, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addMatch(request):
    match = Match.objects.create(
        team1=1,
        team2=2,
        date='2021-01-01',
        time = '00:00:00',
        team1_score=0,
        team2_score=0,
        category='Sample Category',
    )
    serializer = MatchSerializer(match, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateMatch(request, pk):
    data = request.data
    match = Match.objects.get(_id=pk)
    match.date = data['date']
    match.time = data['time']
    match.team1_score = data['team1_score']
    match.team2_score = data['team2_score']
    match.save()
    serializer = MatchSerializer(match, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteMatch(request, pk):
    match = Match.objects.get(_id=pk)
    match.delete()
    return Response('Match was deleted')

@api_view(['POST'])
def uploadImage(request):
    data = request.data
    match_id = data['match_id']
    match = Match.objects.get(_id=match_id)
    match.image = request.FILES.get('image')
    match.save()
    return Response('Image was uploaded')

@api_view(['GET'])
def getOneLatestMatch(request):
    match = Match.objects.all().order_by('-_id')[:1]
    serializer = MatchSerializer(match, many=True)
    return Response(serializer.data)
