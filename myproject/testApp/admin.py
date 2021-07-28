from django.contrib import admin
from .models import SnsMessageModel,SnsCommentModel

# Register your models here.

admin.site.register(SnsMessageModel)
admin.site.register(SnsCommentModel)