from django.contrib import admin
from .models import ProjectConfig

@admin.register(ProjectConfig)
class ProjectConfigAdminModel(admin.ModelAdmin):
    
    list_display = (
        'project_id', 'name', 'description', 'user', 'project_type', 'created', 'updated', 'target_audience', 'core_features', 'challenges', 'action_items'
    )