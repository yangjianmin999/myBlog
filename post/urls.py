from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index_view),
    url(r'^page/(\d+)$',views.index_view),
    url(r'^post/(\d+)$',views.post_view),
    url(r'^category/(\d+)$',views.cate_view),
    url(r'^archive/(\d{4})/(\d{2})$',views.archive_view),
    url(r'^archive/$',views.archive_view),
    url(r'^aboutme/$',views.aboutme_view),
    url(r'^search/',views.search_view),
]



















