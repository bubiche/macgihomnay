from django.conf.urls import patterns, url
from image_search import views


urlpatterns = patterns(
    '',
    url(r'^search$', views.search, name='image_search'),
)
