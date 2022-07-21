from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ProjectConfig(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    project_type = models.IntegerField(default=0)
    target_audience = models.CharField(max_length=2000, default=[])
    core_features = models.CharField(max_length=2000, default=[])
    challenges = models.CharField(max_length=2000, default=[])
    action_items = models.CharField(max_length=2000, default=[])

    def __str__(self) -> str:
        return self.name