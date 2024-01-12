from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from core.user.serializers.create import UserCreationSerializer

class UserCreateView(APIView):
    """
    Create/register a user with:
    - email
    - first name
    - last name 
    - password
    """
    serializer_class = UserCreationSerializer

    def post(self, request):
        """
        Create user
        """

        serializer = UserCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)