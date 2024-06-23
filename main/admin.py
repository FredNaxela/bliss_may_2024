from django.contrib import admin
from .models import Banner, Services, About, Price, Reviews, Blog, Contact, Session, Category
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

# Register your models here.

admin.site.register(Contact)
admin.site.register(Session)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'title', 'description','sort')
    list_editable = ('sort',)
    list_filter = ('sort',)


@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ('image_src_tag1', 'image_src_tag2', 'description', 'sort')
    list_editable = ('sort',)
    list_filter = ('sort',)

    def image_src_tag1(self, obj):
        if obj.image1:
            return mark_safe(f"<img src='{obj.image1.url}' width=50 height=50>")

    def image_src_tag2(self, obj):
        if obj.image2:
            return mark_safe(f"<img src='{obj.image2.url}' width=50 height=50>")


@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    list_display = ('image_src_tag', 'name', 'description', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'Service image'


@admin.register(Price)
class PriceAdmin(TranslationAdmin):
    list_display = ('name', 'description', 'price', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('image_src_tag', 'name', 'description', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'Blog image'


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('image_src_tag', 'name', 'description', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'About image'


@admin.register(Reviews)
class ReviewsAdmin(TranslationAdmin):
    list_display = ('image_src_tag', 'name', 'description', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'Review image'