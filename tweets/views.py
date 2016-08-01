from django.shortcuts import render
from django.views.generic import View 
from .models import Tweet
from django.contrib.auth.models import User 
#from .forms import PostForm

class ListView(View):
	def get(self, request):
		template_name = "tweets/list.html"
		tweets = Tweet.objects.all()
		context = {'tweets': tweets}
		return render(request, template_name, context)

class  DetailView(View):
	def get(self, request, id):
		template_name = "tweets/detail.html"
		tweets = Tweet.objects.get(id=id)
		context = {'tweet': tweets}
		return render(request, template_name, context)

