from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from faq import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
	url(r'^faq/', include('faq.urls', namespace="faq"))
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""if not settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)
"""