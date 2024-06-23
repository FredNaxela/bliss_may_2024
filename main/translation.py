from modeltranslation.translator import register, TranslationOptions
from .models import Banner, Services, About, Price, Reviews, Blog, Category


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Price)
class PriceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
