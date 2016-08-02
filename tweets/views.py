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
		tw = Tweet.objects.get(id=id)
		context = {'tweet': tw}
		return render(request, template_name, context)

class NuevoPost(View):
	def get(self,request):
		template_name = 'tweets/nuevo.html'
		context = {}
		return render(request,template_name,context)

	def post(self,request):
		print('hola')
		username = request.POST.get('username')
		content = request.POST.get('content')
		post = Tweet()
		post.username = username
		post.content = content
		post.usuario = request.user
		post.save()

		template_name = 'tweets/nuevo.html'
		context = {'guardado':True}

		return render(request,template_name,context) 

