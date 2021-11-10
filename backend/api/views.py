from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def hello_api(request):
    print('############ 0 ##########')
    return Response({'message': "Server Started !"})