from django.shortcuts import render
from django.views.generic import TemplateView

from demo_app.models import SiteHeaderItem, RentCategory, Villa, Promotion, Article, CustomerReview, News


class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['header_items'] = SiteHeaderItem.objects.all()
        data['rent_category'] = RentCategory.objects.all()
        data['main_villa'] = Villa.objects.filter(name__contains='Жемчужина').first()
        data['promotion'] = Promotion.objects.filter(title__contains='Аренда').first()
        data['popular_villas'] = Villa.objects.filter(rating__gt=3)
        data['articles'] = Article.objects.all()
        data['recommendations'] = Villa.objects.filter(is_recommended=True)
        data['customer_reviews'] = CustomerReview.objects.all()[:5]
        data['news'] = News.objects.all()[:5]
        # print(datpipa)
        return data
