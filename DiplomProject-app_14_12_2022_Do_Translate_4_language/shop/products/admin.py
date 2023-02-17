from django.contrib import admin
from .models import Category, Product
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class ProductCategoryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdminForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorUploadingWidget())
    description = forms.CharField(widget=CKEditorUploadingWidget())
    short_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    # list_display = ['id', 'name', 'description', 'time']
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # 'description')
    # list_editable = ('description',)
    list_filter = ('name',)


class ProductAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'category','slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    list_display_links = ('id', 'name')
    # list_filter = ('time',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
