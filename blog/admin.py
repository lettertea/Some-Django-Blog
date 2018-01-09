from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
