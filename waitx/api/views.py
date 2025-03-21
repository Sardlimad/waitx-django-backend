from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InscripcionPriorizada
from .serializers import InscripcionPriorizadaSerializer

class InscripcionPriorizadaListCreate(APIView):
    def get(self, request):
        inscripciones = InscripcionPriorizada.objects.all()
        serializer = InscripcionPriorizadaSerializer(inscripciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscripcionPriorizadaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
