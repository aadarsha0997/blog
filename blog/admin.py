from django.contrib import admin
from .models import Post,Author,Tag


class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name","email",)
class TagAdmin(admin.ModelAdmin):
    list_display=("caption",)
class PostAdmin(admin.ModelAdmin):
    list_display=("title",)
    list_filter=("date","author",)


# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)