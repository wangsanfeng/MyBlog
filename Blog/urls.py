from django.conf.urls import patterns, include, url
from django.contrib import admin
from Article.views import RSSFeed,AboutView
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','Article.views.home'),
    url(r'^(?P<id>\d+)/$','Article.views.detail',name = 'detail'),
    url(r'^test/$','Article.views.test'),
    url(r'^archives/$', 'Article.views.archives', name = 'archives'),
    # url(r'^aboutme/$', 'Article.views.about_me', name = 'about_me'),
    url(r'^aboutme/$',AboutView.as_view(),name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$', 'Article.views.search_tag', name = 'search_tag'),
    url(r'^search/$','Article.views.blog_search', name = 'search'),
    url(r'^feed/$',RSSFeed(),name = 'RSS'),
)
