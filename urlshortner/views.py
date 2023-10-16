import traceback

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (CreateShortURISerializer, UpdateShortURISerializer,
                          UpdateExpirySerializer, GetAllDataSerializer)
from .models import URLStore
from urlshortner.utils.utility import BL
from datetime import datetime, date, timedelta


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
                shortenURI = BL.generateShortURI()
                uriInstance = URLStore.objects.create(originaluri=valid_data['originalUrl'],
                                                      shorturi=shortenURI,
                                                      expiryAt=valid_data['expiryDate'])
                uriInstance.save()
                return Response(data={"id": uriInstance.id, "shortenUri": shortenURI},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            tb = traceback.format_exc()
            print(tb)
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
                    uriInstance.expiryAt = validatedData['expiryDate']
                    uriInstance.save()
                    return Response(data={"msg": "Original URI updated successfully."}, status=status.HTTP_200_OK)
                return Response(data={"msg": "Short URI does not exists."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msg": 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RedirectApiView(APIView):

    def get(self, request, shorturi):
        try:
            originalUrl = URLStore.objects.get(shorturi=shorturi)
            response = Response(data={},status=status.HTTP_302_FOUND)
            response['Location'] = originalUrl.originaluri
            response['Content-Type'] = 'application/json'
            return response
        except URLStore.DoesNotExist:
            return Response(data={"msg": "Resource not found"}, status=404)
        except Exception as e:
            tb = traceback.format_exc()
            print(tb)
            return Response(data={"msg": 'Something went wrong.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
