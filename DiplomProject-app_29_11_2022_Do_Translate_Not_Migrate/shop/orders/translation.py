from modeltranslation.translator import TranslationOptions, register

from .models import Order


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'address',
              'city')


# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('name',)
