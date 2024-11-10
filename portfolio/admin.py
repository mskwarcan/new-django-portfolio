from django.contrib import admin
from .models import Project
from .models import Tag
from .models import Image

# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Image)