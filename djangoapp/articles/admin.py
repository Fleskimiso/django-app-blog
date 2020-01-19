from django.contrib import admin
from .models import Article

#we arew telling django to register somethingo in a admin site
admin.site.register(Article)

# Register your models here.
