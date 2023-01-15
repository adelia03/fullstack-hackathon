from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import User
from .serializers import RegisterSerializer


class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        # print(request.data)
        serializer = RegisterSerializer(data=request.data)
        # print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Вы успешно зарегистрировались", status=201)
    

class DeleteUserView(APIView):
    def delete(self, request, email):
        user = get_object_or_404(User, email=email)
        if user.is_staff: #or user != request.user:
            return Response(status=403) #запрещаем
        user.delete()
        return Response(status=204)

@api_view(['GET'])
def activate_view(request, activation_code):
    user = get_object_or_404(User, activation_code=activation_code)
    user.is_active = True # activate user
    user.activation_code = '' # delete the activated code
    user.save()
    return Response('Successfuly activated the account', 200)