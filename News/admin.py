from django.contrib import admin
from .models import News, Comment      
from django_summernote.admin import SummernoteModelAdmin

@admin.register(News)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('news_content')
    prepopulated_fields = {'slug': ('news_title',)}
    list_filter = ('released_status', 'created_on')
    search_fields = ['news_title', 'news_content']
    list_display = ('news_title', 'slug', 'released_status', 'created_on')
        
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'Comment_content', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user_name', 'Comment_content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)





