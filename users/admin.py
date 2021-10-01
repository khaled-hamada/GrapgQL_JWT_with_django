from django.contrib import admin
from django.apps import apps
# Register your models here.

from .models import ExtendUser
admin.site.register(ExtendUser)

# register django auth app models 
app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
    