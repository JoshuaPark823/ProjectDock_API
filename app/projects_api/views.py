from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import ProjectConfig
from .serializers import ProjectConfigSerializer

class ProjectConfigViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProjectConfigSerializer
    queryset = ProjectConfig.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = ProjectConfig.objects.filter(user = request.user)
        serializer = ProjectConfigSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)