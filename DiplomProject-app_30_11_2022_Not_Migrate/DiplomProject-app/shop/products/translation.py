from modeltranslation.translator import TranslationOptions, register

from .models import Product, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category', 'name', 'description',
              'short_description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
