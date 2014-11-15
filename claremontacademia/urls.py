from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'claremontacademia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index, name='index'),
    url(r'^forums/(?P<forum_name>[a-z]+)/$',views.forum,name='forum'),
    url(r'^forums/[a-z]+/(?P<forum_name>[a-z]+[0-9]+)/$',views.forum,name='forum'),
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^forums/([a-z]+/)?[a-z0-9]+/(?P<id>[0-9]+)/$',views.thread, name='thread'),
    url(r'^post/$',views.post,name='post'),
    url(r'^get_department/(?P<department_name>[a-z]+)/$', views.get_department, name='get_department'),
    url(r'^comment/(?P<thread_id>[0-9]+)/$', views.comment, name='comment'),
    url(r'^admin/', include(admin.site.urls)),
)
