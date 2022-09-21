from django.shortcuts import render
from api.models import CompletedCase, main_data, IntentData, EntityData
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


class NotCompletedCasesPageTemplate(View):
	
	template_name = 'website/Not_completed_cases.html'

	def get(self, request):
		objects = CompletedCase.objects.all()
		sec_objects =  main_data.objects.filter(title="Anxiety Disorders").all()
		headings = [i.case_id.id for i in objects]
		final = [not_completed for not_completed in sec_objects if not_completed.id not in headings]
		my_paginator = Paginator(final, 10)
		page = request.GET.get("page")
		data = my_paginator.get_page(page)

		return render(request, self.template_name, {"data":data})


class IntentCasesPageTemplate(View):
	
	template_name = 'website/intent.html'

	def get(self, request, pk):
		mainobj = main_data.objects.filter(id=pk).first()  
		info =  mainobj
		title = info.sub_heading
		case = info.main_problem
		case_ids = info.id
			
		return render(request, self.template_name, 
				{"title":title, "case":case, 
				"case_id":case_ids})


class UpdateIntentCasesTemplate(View):

	template_name = 'website/update-intent.html'

	def get(self, request, pk):

		mainobj = main_data.objects.filter(id=pk).first()
		obj = CompletedCase.objects.filter(case_id.id=pk).first()
		intent = None
		if obj:
			data = obj
			intent = data.intent
		info =  mainobj
		title = info.sub_heading
		case = info.main_problem
		case_ids = info.id
			
		return render(request, self.template_name, 
				{"title":title, "case":case, 
				"case_id":case_ids, "intent":intent})

class EntityCasesPageTemplate(View):

	template_name = 'website/Entity.html'

	def get(self, request, pk):
		keywords_list = []
		mainobj = main_data.objects.filter(id=pk) 
		obj = IntentData.objects.filter(case_id=mainobj)
		if mainobj:
			info = mainobj[0]
			title = info.sub_heading
			case = info.main_problem
			case_ids = info.id
		if obj:
			for key in obj:
				keyword = key.entity
				keywords_list.append(keyword)

		return render(request, self.template_name, 
				{"title":title, "case":case, 
				"case_id":case_ids, "keyword":keywords_list})