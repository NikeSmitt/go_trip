from django.contrib import admin

from demo_app.models import SiteHeaderItem, Villa, RentCategory, Car, Tour, Bike, VillaImage, Promotion, Article, \
    ArticleImage, CustomerReview, News


@admin.register(SiteHeaderItem)
class SiteHeaderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']


@admin.register(VillaImage)
class VillaImageAdmin(admin.ModelAdmin):
    # list_display = ['id', 'album']
    pass


class VillaImageInline(admin.TabularInline):
    model = VillaImage
    extra = 3


@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    inlines = [VillaImageInline, ]
    list_display = ['id', 'name', 'rating']


@admin.register(RentCategory)
class RentCategory(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Promotion)
class Promotion(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline, ]
    list_display = ['id', 'title']


@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'body']
    
    

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass