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
from core.factory import temp_context_data, get_client_ip
from core.jwt_token import get_access_token 
from core.text_to_sentence import TextToSentence
import logging

class HomeView(TemplateView):
	template_name = "website/index.html"

class MainView(LoginRequiredMixin, View):
	template_name = 'website/main.html'
	login_url = '/login'

	def get(self, request):
		current_user = request.user.username
		logging.error(f"logged User --> {current_user}")
		meta = request.META
		ip = get_client_ip(meta)
		if current_user != "sumir":
			steps = FingerPrints(ip=ip, user=current_user)
			steps.save()
		return render(request, self.template_name)

class CompletedCasesPageTemplate(LoginRequiredMixin, View):
	
	template_name = 'website/Completed_cases.html'
	login_url = '/login'

	def get(self, request):
		objects = CompletedCase.objects.all()
		my_paginator = Paginator(objects, 10)
		page = request.GET.get("page")
		data = my_paginator.get_page(page)
		token = get_access_token()

		return render(request, self.template_name, {"data":data, "token":token})


class NotCompletedCasesPageTemplate(LoginRequiredMixin, View):
	
	template_name = 'website/Not_completed_cases.html'
	login_url = '/login'

	def get(self, request):
		objects = CompletedCase.objects.all()
		sec_objects =  main_data.objects.filter(title="Anxiety Disorders").all()
		headings = [i.case_id.id for i in objects]
		final = [not_completed for not_completed in sec_objects if not_completed.id not in headings]
		my_paginator = Paginator(final, 10)
		page = request.GET.get("page")
		data = my_paginator.get_page(page)
		token = get_access_token()
		return render(request, self.template_name, {"data":data, "token":token})


class IntentCasesPageTemplate(LoginRequiredMixin, View):
	
	template_name = 'website/intent.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		mainobj = main_data.objects.filter(id=pk).first()
		linkobj = LinkConfig.objects.filter(id=pk).first()  
		context = temp_context_data(mainobj, linkobj)
		context['token'] = access_token	
		return render(request, self.template_name, context)


class UpdateIntentCasesTemplate(LoginRequiredMixin, View):

	template_name = 'website/update-intent.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		mainobj = main_data.objects.filter(id=pk).first()
		obj = IntentData.objects.filter(case_id=mainobj).first()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		context = temp_context_data(mainobj, linkobj)
		context["intent"] = obj.intent
		context['token'] = access_token		
		return render(request, self.template_name, context)


class EntityCasesPageTemplate(LoginRequiredMixin, View):

	template_name = 'website/symptoms.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)
		context['token'] = access_token
		return render(request, self.template_name, context)


class UpdateEntityCasesTemplate(LoginRequiredMixin, View):

	template_name = 'website/update-symptoms.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		keywords_list = []
		mainobj = main_data.objects.filter(id=pk).first() 
		linkobj = LinkConfig.objects.filter(id=pk).first()
		obj = EntityData.objects.filter(case_id=mainobj).all()
		context = temp_context_data(mainobj, linkobj)
		keywords_list = [key.entity for key in obj if obj is not None]
		context["keyword"] = keywords_list
		context['token'] = access_token

		return render(request, self.template_name, context)

class CauseCasesPageTemplate(LoginRequiredMixin, View):

	template_name = 'website/cause.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)
		context['token'] = access_token

		return render(request, self.template_name, context)

class UpdatdeCauseTempalte(LoginRequiredMixin, View):

	template_name = 'website/update-cause.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		mainobj = main_data.objects.filter(id=pk).first() 
		linkobj = LinkConfig.objects.filter(id=pk).first()
		causeobj = Cause.objects.filter(case_id=mainobj).first()
		keywordobj = CauseKeyword.objects.filter(case_id=causeobj).all()
		context = temp_context_data(mainobj, linkobj)
		if causeobj:
			context["cause"] = causeobj.cause
		else:
			context["cause"] = None
		keyword = [key.keyword for key in keywordobj if keywordobj is not None]
		context["keyword"] = keyword
		context['token'] = access_token

		return render(request, self.template_name, context)


class PatientAskingForPageTemplate(LoginRequiredMixin, View):
	
	template_name = 'website/patient_asking_for.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)
		context['token'] = access_token
		return render(request, self.template_name, context)

class UpdatePatientAskingForTemplate(LoginRequiredMixin, View):

	template_name = 'website/update_patient_asking_for.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		mainobj = main_data.objects.filter(id=pk).first() 
		linkobj = LinkConfig.objects.filter(id=pk).first()
		pafobj = PatientAskingFor.objects.filter(case_id=mainobj).first()
		keywordobj = PatientAskingForKeyword.objects.filter(case_id=pafobj).all()
		context = temp_context_data(mainobj, linkobj)
		if pafobj:
			context["need"] = pafobj.asking
		else:
			context["need"] = None
		keyword = [key.keyword for key in keywordobj if keywordobj is not None]
		context["keyword"] = keyword
		context['token'] = access_token
		return render(request, self.template_name, context)


class HistoryPageTemplate(LoginRequiredMixin, View):

	template_name = 'website/history.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)
		context['token'] = access_token
		sentences_list = TextToSentence(mainobj.main_problem).text_to_sentence_list()
		context["sentence"] = sentences_list
		return render(request, self.template_name, context)


class UpdateHistoryTemplate(LoginRequiredMixin, View):

	template_name = 'website/update-history.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		mainobj = main_data.objects.filter(id=pk).first()
		obj = History.objects.filter(case_id=mainobj).all()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		context = temp_context_data(mainobj, linkobj)
		keyword = [key.keyword for key in obj if obj is not None]
		context["keyword"] = keyword
		context["token"] = access_token
		sentences_list = TextToSentence(mainobj.main_problem).text_to_sentence_list()
		context["sentence"] = sentences_list
		return render(request, self.template_name, context)


class EffectPageTemplate(LoginRequiredMixin, View):

	template_name = 'website/effect.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()

		linkobj = LinkConfig.objects.filter(id=pk).first()
		mainobj = main_data.objects.filter(id=pk).first() 
		context = temp_context_data(mainobj, linkobj)
		context['token'] = access_token
		return render(request, self.template_name, context)


class UpdateEffectTemplate(LoginRequiredMixin, View):

	template_name = 'website/update-effect.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		mainobj = main_data.objects.filter(id=pk).first()
		obj = Effect.objects.filter(case_id=mainobj).all()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		context = temp_context_data(mainobj, linkobj)
		keyword = [key.keyword for key in obj if obj is not None]
		context["keyword"] = keyword
		context['token'] = access_token	
		return render(request, self.template_name, context)

class UpdateMainDataTemplate(LoginRequiredMixin, View):

	template_name = 'website/update-main-data.html'
	login_url = '/login'

	def get(self, request, pk):
		access_token = get_access_token()
		mainobj = main_data.objects.filter(id=pk).first()
		linkobj = LinkConfig.objects.filter(id=pk).first()
		context = temp_context_data(mainobj, linkobj)
		context['token'] = access_token
		return render(request, self.template_name, context)


