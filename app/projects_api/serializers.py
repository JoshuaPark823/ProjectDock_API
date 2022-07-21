from rest_framework import serializers
from .models import ProjectConfig

class ProjectConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectConfig
        fields = (
            '__all__'
        )