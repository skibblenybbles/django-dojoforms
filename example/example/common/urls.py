from django.conf.urls import patterns, include, url

urlpatterns = patterns("example.common.views",
    
    url(r'^$', "pages.homepage_view", name="homepage"),
)
