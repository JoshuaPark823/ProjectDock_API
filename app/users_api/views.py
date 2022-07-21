from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import permissions, status, mixins
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer

class UserDetailsAPIView(RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
            Get a user with the specific ID
        """

        user_instance = User.objects.get(username = request.user)

        # RG: todo switch to serializer
        content = {
            'user_id': int(user_instance.id),
            'username': str(user_instance),
            'first_name': str(user_instance.first_name),
            'last_name': str(user_instance.last_name),
            'email': str(user_instance.email)
        }

        return Response(content, status=status.HTTP_200_OK)

class ProfileAPIView(APIView):

    parser_class = (FileUploadParser,)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        instance = Profile.objects.get(user = request.user)
        serializer = ProfileSerializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):

        user_instance = User.objects.get(username = request.user)
        old_model = Profile.objects.get(user_id = user_instance)

        profile_serializer = ProfileSerializer(instance=old_model, data=request.data)

        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):

        profile_serializer = ProfileSerializer(data=request.data)

        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)