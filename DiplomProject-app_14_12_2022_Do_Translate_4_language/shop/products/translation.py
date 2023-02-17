from modeltranslation.translator import register, TranslationOptions
from products.models import Product, Category


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category', 'name', 'description',
              'description', 'short_description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
