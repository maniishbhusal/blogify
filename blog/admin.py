from django.contrib import admin
from .models import Blog,Contact,BlogComment

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
admin.site.register(BlogComment)