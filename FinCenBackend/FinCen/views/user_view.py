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


class RegisterUser(APIView):
    @swagger_auto_schema(
        request_body=RegisterSerializer,
        operation_summary="Registers the user",
        operation_description="Registers the user and stores it in the User Table",
        responses={201: "Created", 500: "Internal server error"},
    )
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("User Registered Successfully" ,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            return Response(type(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginUser(APIView):
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: "Ok", 500: "Internal server error", 400: "Bad Request", 401: "Unauthorized"}
    )
    def post(self, request):
        try:
            # Validate
            try:
                user_name = request.data[nameof(User.user_name)]
                password = request.data[nameof(User.password)]
            except:
                return Response("Invalid Parameters passed!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # Process and return
            try:
                user = User.objects.get(user_name=user_name)
            except:
                return Response("User not found", status=status.HTTP_400_BAD_REQUEST)
            if user is not None:
                if check_password(password, user.password):
                    return Response({nameof(user.api_key): user.api_key}, status=status.HTTP_200_OK)
                return Response("Username or password is wrong", status=status.HTTP_401_UNAUTHORIZED)
            return Response("User not found", status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response(ResponseUtil.create_generic_response(status.HTTP_500_INTERNAL_SERVER_ERROR, type(err), err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetUser(APIView):
    api_key = openapi.Parameter('api_key', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    @swagger_auto_schema(
        manual_parameters=[api_key],
        response={200: "Ok"}
    )
    def get(self, request):
        try:
            # Validate
            try:
                api_key = request.query_params.get(nameof(User.api_key))
            except:
                return Response("Invalid Parameters passed!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            try:
                user = User.objects.get(api_key=api_key)
                print("Got user")
                if user is not None:
                    print("Inside user is not none")
                    response = model_to_dict(user)
                    return Response(response, status=status.HTTP_200_OK)
            except:
                return Response("API", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            return Response(ResponseUtil.create_generic_response(status.HTTP_500_INTERNAL_SERVER_ERROR, type(err), err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)