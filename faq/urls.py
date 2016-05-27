from django.conf.urls import url

from . import views

urlpatterns = [
	# /faq/
	url(r'^$', views.index, name='index'),
]