from django.contrib import admin
from .models import *

# class PostsAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'date', 'is_publisher']
#     list_display_links = ['id', 'title']
#     list_filter = ['title', 'date']

# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ['id', 'comment', 'user']
#     list_display_links = ['id', 'comment']

admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Prod)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Zakaz)
