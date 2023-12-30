from ..serializers import *
from ..models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..util import ResponseUtil
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import check_password
from drf_yasg import openapi
from django.forms.models import model_to_dict


class AssetInfo(APIView):
    api_key = openapi.Parameter('api_key', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    asset_id = openapi.Parameter('asset_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(
        manual_parameters=[api_key, asset_id],
        response={ 200: "Ok", 401: "Unauthorized", 400: "Bad request" }
    )
    def get(self, request):
        try:
            # Validation and extraction of data
            try:
                api_key = request.query_params.get(nameof(User.api_key))
                asset_id = request.query_params.get(nameof(Asset.asset_id))
                user = User.objects.get(api_key=api_key)
                asset = Asset.objects.get(asset_id=asset_id)
            except:
                return Response("Invalid Parameters passed", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            if user is not None and asset is not None:
                if asset.user.api_key == user.api_key:
                    asset_response_serializer = AssetInfoResponseSerializer(data=model_to_dict(asset))
                    if asset_response_serializer.is_valid():
                        return Response(asset_response_serializer.data, status=status.HTTP_200_OK)
                    return Response(asset_response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
            return Response("Some error occurred", stauts=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as err:
            return Response(ResponseUtil.create_generic_response(status.HTTP_500_INTERNAL_SERVER_ERROR, type(err), err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddAsset(APIView):
    @swagger_auto_schema(
        request_body=SaveAssetPayloadSerializer,
        responses={201: "Created", 500: "Internal server error"},
    )
    def post(self, request):
        try:
            request_payload = request.data
            try:
                payload = SaveAssetPayloadSerializer(data=request_payload)
                if payload.is_valid():
                    validated_data = payload.validated_data
                    api_key = validated_data.get('api_key')
                    user = User.objects.get(api_key=api_key)
                else:
                    return Response(f"Validation Error, {payload.errors}", status=status.HTTP_400_BAD_REQUEST) 
            except:
                return Response("Validation Error", status=status.HTTP_400_BAD_REQUEST)
            
            if user is not None:
                data_to_save = validated_data
                data_to_save[nameof(Asset.user)] = user.id
                asset_serializer = AssetSerializer(data=data_to_save)
                if asset_serializer.is_valid():
                    asset_serializer.save()
                    return Response("Asset Data Created!", status=status.HTTP_201_CREATED)
                return Response(f"Errors: {asset_serializer.errors}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)

        except Exception as err:
            return Response(ResponseUtil.create_generic_response(status.HTTP_500_INTERNAL_SERVER_ERROR, type(err), err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetAllAssets(APIView):
    api_key = openapi.Parameter('api_key', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    @swagger_auto_schema(
        manual_parameters=[api_key],
        response={ 200: "Ok", 401: "Unauthorized", 400: "Bad request" }
    )
    def get(self, request):
        try:
            try:
                api_key = request.query_params.get(nameof(User.api_key))
                user = User.objects.get(api_key=api_key)
            except:
                return Response("Validation Error", status=status.HTTP_400_BAD_REQUEST)
            
            if user is not None:
                assets = Asset.objects.filter(user=user.id).values()
                return Response(assets, status.HTTP_200_OK)
            return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as err:
            return Response(ResponseUtil.create_generic_response(status.HTTP_500_INTERNAL_SERVER_ERROR, type(err), err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)