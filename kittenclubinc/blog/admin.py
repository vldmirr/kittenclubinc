from django.contrib import admin
from .models import Post
# Register your models here.

#adding a new entity 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','status']#1
    list_filter=['status','created','publish','author']#2
    search_fields=['status','created','publish','author']
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=['author']
    date_hierarchy='publish'
    ordering=['status','publish']
#admin.site.register(Post)