from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ListView.as_view(), name="list"),
	url(r'^(?P<id>\d+)$', views.DetailView.as_view(), name="details")
]