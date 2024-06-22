from django.contrib import admin
from .models import Banner, Services, About, Price, Reviews, Blog, Contact, Session
from django.utils.safestring import mark_safe


# Register your models here.

admin.site.register(Contact)
admin.site.register(Session)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
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
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('image_src_tag', 'name', 'description', 'category', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'Service image'


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('image_src_tag', 'name', 'description', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'Blog image'


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image_src_tag', 'name', 'description', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'About image'


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('image_src_tag', 'name', 'description', 'sort')
    list_editable = ('sort',)
    search_fields = ('name',)
    list_filter = ('sort',)

    def image_src_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")

    image_src_tag.short_description = 'Review image'