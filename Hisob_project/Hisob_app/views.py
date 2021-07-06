from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Shart, Bajarish
from .serializers import ShartSerializer, BajarishSerializer


@api_view(['GET', 'POST'])
def shart_list(request):
    if request.method == 'GET':
        shart = Shart.objects.all()
        serializers = ShartSerializer(shart, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ShartSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def shart_post(request, pk):
    try:
        bajar = Shart.objects.get(pk=pk)
    except bajar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShartSerializer(bajar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShartSerializer(bajar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bajar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Amal uchun
@api_view(['GET', 'POST'])
def bajar_list(request):
    if request.method == 'GET':
        bajar = Bajarish.objects.all()
        serializers = BajarishSerializer(bajar, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = BajarishSerializer(data=request.data)
        serializers.is_valid(raise_exception=False)
        serializers.create(serializers.data)
        return Response({"ok": "qoshildi"})


@api_view(['GET', 'PUT', 'DELETE'])
def bajar_post(request, pk):
    try:
        bajar = Bajarish.objects.get(pk=pk)
    except bajar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BajarishSerializer(bajar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BajarishSerializer(bajar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bajar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


