from django.conf.urls import include, url
from django.contrib import admin

from faq import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
	url(r'^faq/', include('faq.urls', namespace="faq"))
]
