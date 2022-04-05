# from re import search
# from unicodedata import name

# from xml.etree.ElementInclude import include
from django import urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from . import views


urlpatterns=[
    url('^$',views.news_today,name='newsToday'),
    url('^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url('^search/', views.search_results, name='search_results'),
    url('^article/(\d+)',views.article,name='article'),
    url('^new/article$', views.new_article, name='new-article')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)