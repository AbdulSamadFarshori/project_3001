from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from api.models import (
						CompletedCase, main_data, 
						IntentData, EntityData, LinkConfig,
						Cause, CauseKeyword,PatientAskingFor,
						History,Effect,PatientAskingForKeyword
						)
from django.views.generic import TemplateView
from django.views import View, generic
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator 
from core.factory import user_is_valid, get_client_ip
from django.shortcuts import redirect
from .models import FingerPrints
from core.factory import temp_context_data 
import logging

class HomeView(TemplateView):
	template_name = "website/index.html"

class MainView(LoginRequiredMixin, View):
	template_name = 'website/main.html'
	def get(self, request):
		current_user = request.user.username
		meta_data = request.META.get('HTTP_X_FORWARDED_FOR')
		ip= ""
		if meta_data:
			ip = meta_data.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		if current_user != "sumir":
			steps = FingerPrints(ip=ip, user=current_user)
			steps.save()
		return render(request, self.template_name)


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
		linkobj = LinkConfig.objects.filter(id=pk).first()  
		context = temp_context_data(mainobj, linkobj)
			
		return render(request, self.template_name, context)


class UpdateIntentCasesTemplate(View):

	template_name = 'website/update-intent.html'

	def get(self, request, pk):

		mainobj = main_data.objects.filter(id=pk).first()
		obj = IntentData.objects.filter(case_id=mainobj).first()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		context = temp_context_data(mainobj, linkobj)
		context["intent"] = obj.intent	
		return render(request, self.template_name, context)


class EntityCasesPageTemplate(View):

	template_name = 'website/symptoms.html'

	def get(self, request, pk):
		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)

		return render(request, self.template_name, context)


class UpdateEntityCasesTemplate(View):

	template_name = 'website/update-symptoms.html'

	def get(self, request, pk):
		keywords_list = []
		mainobj = main_data.objects.filter(id=pk).first() 
		linkobj = LinkConfig.objects.filter(id=pk).first()
		obj = EntityData.objects.filter(case_id=mainobj).all()
		context = temp_context_data(mainobj, linkobj)
		keywords_list = [key.entity for key in obj]
		context["keyword"] = keywords_list

		return render(request, self.template_name, context)

class CauseCasesPageTemplate(View):

	template_name = 'website/cause.html'

	def get(self, request, pk):
		
		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)

		return render(request, self.template_name, context)

class UpdatdeCauseTempalte(View):

	template_name = 'website/update-cause.html'

	def get(self, request, pk):
		
		mainobj = main_data.objects.filter(id=pk).first() 
		linkobj = LinkConfig.objects.filter(id=pk).first()
		causeobj = Cause.objects.filter(case_id=mainobj).first()
		keywordobj = CauseKeyword.objects.filter(case_id=causeobj).all()
		context = temp_context_data(mainobj, linkobj)
		context["cause"] = causeobj.cause
		keyword = [key.keyword for key in keywordobj]
		context["keyword"] = keyword

		return render(request, self.template_name, context)


class PatientAskingForPageTemplate(View):
	
	template_name = 'website/patient_asking_for.html'

	def get(self, request, pk):

		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)

		return render(request, self.template_name, context)

class UpdatePatientAskingForTemplate(View):

	template_name = 'website/update_patient_asking_for.html'

	def get(self, request, pk):

		mainobj = main_data.objects.filter(id=pk).first() 
		linkobj = LinkConfig.objects.filter(id=pk).first()
		pafobj = PatientAskingFor.objects.filter(case_id=mainobj).first()
		keywordobj = PatientAskingForKeyword.objects.filter(case_id=pafobj).all()
		context = temp_context_data(mainobj, linkobj)
		context["need"] = pafeobj.cause
		keyword = [key.keyword for key in keywordobj]
		context["keyword"] = keyword

		return render(request, self.template_name, context)


class HistoryPageTemplate(View):

	template_name = 'website/history.html'

	def get(self, request, pk):

		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)

		return render(request, self.template_name, context)


class UpdateHistoryTemplate(View):

	template_name = 'website/update-history.html'

	def get(self, request, pk):

		mainobj = main_data.objects.filter(id=pk).first()
		obj = History.objects.filter(case_id=mainobj).first()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		context = temp_context_data(mainobj, linkobj)
		keyword = [key.keyword for key in obj]
		context["keyword"] = keyword	
		return render(request, self.template_name, context)


class EffectPageTemplate(View):

	template_name = 'website/effect.html'

	def get(self, request, pk):

		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)

		return render(request, self.template_name, context)


class UpdateEffectTemplate(View):

	template_name = 'website/update-effect.html'

	def get(self, request, pk):

		mainobj = main_data.objects.filter(id=pk).first()
		obj = Effect.objects.filter(case_id=mainobj).first()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		context = temp_context_data(mainobj, linkobj)
		keyword = [key.keyword for key in obj]
		context["keyword"] = keyword	
		return render(request, self.template_name, context)