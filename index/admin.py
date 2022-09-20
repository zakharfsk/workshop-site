from django.contrib import admin

from .models import MyProject, MyJobExperience, MySkills

# Register your models here.

admin.site.register(MyProject)
admin.site.register(MyJobExperience)
admin.site.register(MySkills)
