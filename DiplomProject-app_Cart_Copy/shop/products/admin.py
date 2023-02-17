# from django.contrib import admin
# from .models import ProductCategory, Product, Basket
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from django import forms
#
#
# class ProductAdminForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget())
#     short_description = forms.CharField(widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class ProductCategoryAdminForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class ProductAdmin(admin.ModelAdmin):
#     form = ProductAdminForm
#     prepopulated_fields = {"slug": ("name",)}
#     list_display = ('id', 'name', 'quantity', 'price',
#                     'category', 'short_description',
#                     'description', 'image',
#                     'time', 'time_update',
#                     )
#     list_display_links = ('id', 'name')
#     search_fields = ('name', 'description', 'short_description')
#     list_editable = ('short_description', 'description')
#     list_filter = ('time',)
#     ordering = ("-time",)
#
#
# class ProductCategoryAdmin(admin.ModelAdmin):
#     form = ProductCategoryAdminForm
#     prepopulated_fields = {"slug": ("name",)}
#     list_display = ('id', 'name', 'description', 'time')
#     list_display_links = ('id', 'name')
#     search_fields = ('name', 'description')
#     list_editable = ('description',)
#     list_filter = ('time',)
#
#
# admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductCategory, ProductCategoryAdmin)
# admin.site.register(Basket)
#
# admin.site.site_header = "Админ-Панель Магазина"
# admin.site.site_title = "Админ-Панель Магазина"


from django.contrib import admin
from .models import Category, Product
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


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


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    list_display_links = ('id', 'name')
    # list_filter = ('time',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
