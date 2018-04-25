from django.conf.urls import include, url
from django.contrib import admin
from . import view
from TestModel import search
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', view.hello),
    url(r'^search-form$',search.search_form),
    url(r'^search$',search.search),
]
