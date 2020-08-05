from django import forms
from django.contrib import admin
from .models import BlogPost

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(label='Текст публикации', widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'slug', 'title', 'timestamp', 'publish_date', 'updated')
    form = BlogPostAdminForm

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostAdmin)