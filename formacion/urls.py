from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from faq import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
	url(r'^faq/', include('faq.urls', namespace="faq"))
]
