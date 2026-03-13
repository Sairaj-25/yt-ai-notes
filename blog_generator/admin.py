# Register your models here.
from django.contrib import admin
from blog_generator.models import BlogPost


@admin.register(BlogPost)
class BlogPostadmin(admin.ModelAdmin):
    readonly_fileds = [field.name for field in BlogPost._meta.fields]

    def has_add_permission(self, request):
        return False
