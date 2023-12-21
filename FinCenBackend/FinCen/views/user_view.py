from ..serializers import *
from ..models import *
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from ..util import ResponseUtil
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import check_password


class RegisterUser(APIView):
    @swagger_auto_schema(
        request_body=RegisterSerializer,
        operation_summary="Registers the user",
        operation_description="Registers the user and stores it in the User Table",
        responses={201: "Created", 500: "Internal server error"},
    )
    def post(self, request):
        try:
            request_data = JSONParser().parse(request)
            serializer = RegisterSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response("User Registered Successfully" ,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            return Response(type(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class LoginUser(APIView):
    @swagger_auto_schema(
    request_body=LoginSerializer,
    responses={200: "Ok", 500: "Internal server error", 400: "Bad Request", 401: "Unauthorized"},
)
    def post(self, request):
        try:
            request_data = JSONParser().parse(request)
            user_name = request_data['user_name']
            try:
                user = User.objects.get(user_name=user_name)
            except:
                return Response("User not found", status=status.HTTP_400_BAD_REQUEST)
            if user is not None:
                if check_password(request_data[nameof(User.password)], user.password):
                    return Response({nameof(user.api_key): user.api_key}, status=status.HTTP_200_OK)
                return Response("Username or password is wrong", status=status.HTTP_401_UNAUTHORIZED)
            return Response("User not found", status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response(ResponseUtil.create_generic_response(status.HTTP_500_INTERNAL_SERVER_ERROR, type(err), err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        