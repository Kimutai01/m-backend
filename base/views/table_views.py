from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from base.serializer import TableSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from base.models import Table
from datetime import datetime

from django.utils import timezone
from pytz import timezone as tz


@api_view(['GET'])

def getTables(request):
    tables = Table.objects.all()
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTable(request, pk):
    table = Table.objects.get(_id=pk)
    serializer = TableSerializer(table, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addTable(request):
    table = Table.objects.create(
        team = 'Sample Team',
        played = 0,
        won = 0,
        drawn = 0,
        lost = 0,
        goals_for = 0,
        goals_against = 0,
        goal_difference = 0,
        points = 0,
    )
    serializer = TableSerializer(table, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateTable(request, pk):
    data = request.data
    table = Table.objects.get(_id=pk)
    table.team = data['team']
    table.played = data['played']
    table.won = data['won']
    table.drawn = data['drawn']
    table.lost = data['lost']
    table.goals_for = data['goals_for']
    table.goals_against = data['goals_against']
    table.goal_difference = data['goal_difference']
    table.points = data['points']
    table.save()
    serializer = TableSerializer(table, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteTable(request, pk):
    table = Table.objects.get(_id=pk)
    table.delete()
    return Response('Table Deleted')
