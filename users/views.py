from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Register(View):
	def get(self, request):
		template_name="users/register.html"
		form = RegisterForm()
		context = {'form': form}
		return render(request, template_name, context)
	def post(self, request):
		template_name="users/register.html"
		form = RegisterForm(request.POST)
		if form.is_valid():
			form_obj = form.save(commit=False)
			form_obj.user = request.user
			form_obj.set_password(form.cleaned_data['cpassword'])
			form_obj.save()
			profile = Profile()
			profile.user = form_obj
			profile.save()
			return redirect('/tweets')
		else:
			context = {'form': form}
			return render(request, template_name, context)

class Dashboard(View):
	pass


