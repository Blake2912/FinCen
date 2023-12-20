from ..serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from ..util import ResponseUtil


class RegisterUser(APIView):
    def post(self, request):
        request_data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseUtil.create_generic_response(status.HTTP_201_CREATED, "User Registered Successfully", None) ,status=status.HTTP_201_CREATED)
        return Response(ResponseUtil.create_generic_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error", serializer.errors), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



