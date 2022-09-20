from django.shortcuts import render
from api.models import CompletedCase
from django.views.generic import TemplateView
from django.views import View, generic
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator 
from core.factory import user_is_valid, get_client_ip
from django.shortcuts import redirect
from .models import FingerPrints
import logging

class HomeView(TemplateView):
	template_name = "website/index.html"


class LoginView(TemplateView):
	template_name = "website/login.html"


class MainView(View):
	template_name = 'website/new_label.html'
	
	def get(self, request, var):
		meta_data = request.META.get('HTTP_X_FORWARDED_FOR')
		ip= ""
		if meta_data:
			ip = meta_data.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		done_list = [i.case_id.id for i in CompletedCase.objects.all()]
		status = user_is_valid(var)
		if var != "sumir":
			steps = FingerPrints(ip=ip, user=var)
			steps.save()
		if status:
			return render(request, self.template_name, {"context":var, "done_list":done_list})
		return redirect("login")


class CompletedCasesPageTemplate(View):
	
	template_name = 'website/Completed_cases.html'

	def get(self, request):
		objects = CompletedCase.objects.all()
		my_paginator = Paginator(objects, 10)
		page = request.GET.get("page")
		data = my_paginator.get_page(page)

		return render(request, self.template_name, {"data":data})	
