from django.conf.urls import url
from django.contrib import admin

from bookmark import views as bk_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', bk_views.index, name='index'),
    url(r'^login$', bk_views.login, name='login'),
    url(r'^check_login', bk_views.check_login, name='check_login'),
    url(r'^logout$', bk_views.logout, name='logout'),
    url(r'^logout$', bk_views.logout, name='logout'),
    url(r'^logout_process', bk_views.logout_process, name='logout_process'),
    url(r'^user_registration_process', bk_views.user_registration_process, name='user_registration_process'),
    url(r'^bookmark$', bk_views.bookmark, name='bookmark'),
    url(r'^bookmark_list$', bk_views.bookmark_list, name='bookmark_list'),
    url(r'^bookmark_detail/(?P<id>[0-9]+)$', bk_views.bookmark_detail, name='bookmark_detail'),
    url(r'^post_comment$', bk_views.post_comment, name='post_comment'),


]

