import traceback

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (CreateShortURISerializer, UpdateShortURISerializer,
                          UpdateExpirySerializer, GetAllDataSerializer)
from .models import URLStore
from uuid import uuid4

from datetime import datetime, date, timedelta


# Create your views here.

class ShortURI(APIView):

    def get(self, request, id=None):
        try:
            if id is None:
                queryset = URLStore.objects.all()
                serializer = GetAllDataSerializer(queryset, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            response = URLStore.objects.filter(id=id)
            if response.exists():
                response_data = list(response.values())[0]
                return Response(data={"Original URI ": response_data['originaluri'],
                                      "short URI ": response_data['shorturi'],
                                      "Expire In ": response_data['expiryAt']}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "URI does not exists."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            tb = traceback.format_exc()
            print(tb)
            return Response({"msg": 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            data = request.data
            serializer = CreateShortURISerializer(data=data)
            if serializer.is_valid():
                valid_data = dict(serializer.validated_data)
                uriInstance = URLStore.objects.create(originaluri=valid_data['originalURI'])
                uriInstance.shorturi = "http://localhost:8000/" + str(uuid4()).split("-")[-1]
                uriInstance.expiryAt = valid_data['expireDay']
                uriInstance.save()
                return Response({"msg": "Short uri generated successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            tb = traceback.format_exc()
            print(tb)
            return Response({"msg": 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            data = request.data
            serializer = UpdateShortURISerializer(data=data)
            if serializer.is_valid():
                validatedData = dict(serializer.validated_data)
                uri_obj = URLStore.objects.filter(shorturi=validatedData['shorturi'])
                if uri_obj.exists():
                    uriInstance = URLStore.objects.get(shorturi=validatedData['short'])
                    uriInstance.originaluri = validatedData['originalURI']
                    uriInstance.save()
                    return Response(data={"msg": "Original URI updated successfully."}, status=status.HTTP_200_OK)
                return Response(data={"msg": "Short URI does not exists."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        try:
            data = request.data
            serializer = UpdateExpirySerializer(data=data)
            if serializer.is_valid():
                validatedData = dict(serializer.validated_data)
                uri_obj = URLStore.objects.filter(shorturi=validatedData['shortURI'])
                if uri_obj.exists():
                    uriInstance = URLStore.objects.get(shorturi=validatedData['shortURI'])
                    uriInstance.expiryAt = validatedData['expireDay']
                    uriInstance.save()
                    return Response(data={"msg": "Original URI updated successfully."}, status=status.HTTP_200_OK)
                return Response(data={"msg": "Short URI does not exists."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
