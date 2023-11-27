from django.contrib.syndication.views import Feed

from .models import Category, AllService, Gallery


class CategoryFeed(Feed):
    title_template = 'category'
    link = 'category-feeds/'
    description_template = '''We will ad new features from Category into this template'''
    
    def allCategory(self):
        return Category.objects.order_by('title')[:10]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.description


# class AllServiceFeed(Feed):
#     def allService(self):
#         return AllService.objects.all()


# class GalleryFeed(Feed):
#     def allGallery(self):
#         return Gallery.objects.all()
