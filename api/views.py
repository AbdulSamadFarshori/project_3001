from django.shortcuts import render
from rest_framework import generics
from api.serializers import (MainData, 
							ReplyDataSerializer, 
							ReplyThreadSerializer, 
							LinkConfigSerializer
							) 
from api.models import (main_data, ReplyData, 
						response, ReplyThread,
						keywords, Cause, CauseKeyword, 
						CompletedCase,
						LinkConfig, 
						EntityData,Effect, 
						IntentData, History,
						PatientAskingFor, PatientAskingForKeyword) 
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination_veiw import MyPagination
from django.contrib.auth import get_user_model
from rest_framework import status
from core.factory import( authenticated, create_hash_key, make_hash, 
						create_user, get_new_list_entity, 
						get_new_list_asking, get_new_list_history, 
						get_new_list_effect, get_new_list_cause
						)
from rest_framework.permissions import IsAuthenticated
from website.models import Cookies
import logging


class IntentApiView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		intent = request.POST.get("intent")
		case_id = request.POST.get("id")
		main_object = main_data.objects.filter(id=case_id).first()
		if intent:
			foo = IntentData(case_id=main_object, intent=intent)
			foo.save()
			return Response({"response":"intent has been added!"})
		return Response({"response": "Bad Request"})

	def put(self, request):
		new_value = request.POST.get("intent")
		case_id = request.POST.get("id")
		main_object = main_data.objects.filter(id=case_id).first()
		intentobj = IntentData.objects.filter(case_id=main_object).first()
		if intentobj:
			intentobj.intent = new_value
			intentobj.save()
			return Response({"response":"intent has been updated!"})
		return Response({"response": "Bad Request"})

class SymptomsApiView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		entity = request.POST.getlist("entity[]")
		case_id = request.POST.get("id")
		main_object = main_data.objects.filter(id=case_id).first()
		if entity:
			for ele in entity:
				foo1 = EntityData(case_id=main_object, entity=ele)
				foo1.save()
			return Response({"response":"symptoms has been added!"})
		return Response({"response": "Bad Request"})

	def put(self, request):

		permission_classes = (IsAuthenticated,)
		new_symptoms = request.POST.getlist("entity[]")
		case_id = request.POST.get("id")
		main_object = main_data.objects.filter(id=case_id).first()
		entobjs = EntityData.objects.filter(case_id=main_object).all()
		old_symptoms = [ent.entity for ent in entobjs]
		check = get_new_list_entity(old_symptoms, new_symptoms, entobjs, main_object)
		if check:
			return Response({"response":"symptoms has been updated!"})
		return Response({"response": "Bad Request"})


class CauseApiView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		
		new_value = request.POST.get("intent")
		case_id = request.POST.get("id")
		entity = request.POST.getlist("entity[]")
		if entity and new_value:
			main_object = main_data.objects.filter(id=case_id).first()
			new_obj = Cause(case_id=main_object, cause=new_value)
			new_obj.save()
			
			for ele in entity:
				key_obj = CauseKeyword(case_id=new_obj, keyword=keyword)
				key_obj.save()
			return Response({"response":"patient asking has been added!"})
		return Response({"response": "Bad Request"})

	def put(self, request):
		new_value = request.POST.get("intent")
		case_id = request.POST.get("id")
		entity = request.POST.getlist("entity[]")
		if entity and new_value:
			main_object = main_data.objects.filter(id=case_id).first()
			new_obj = Cause.objects.filter(case_id=main_object).first()
			if new_obj:
				new_obj.cause = new_value
				new_obj.save()
			else:
				new_obj = Cause(case_id=main_object, cause=new_value)
				new_obj.save()
			entobjs = CauseKeyword.objects.filter(case_id=new_obj).all()
			old_asking = [ent.keyword for ent in entobjs]
			check = get_new_list_cause(old_asking, entity, entobjs, new_obj)
			if check:
				return Response({"response":"patient asking has been added!"})
		return Response({"response": "Bad Request"}) 

class PatientAskingApiView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		
		new_value = request.POST.get("intent")
		case_id = request.POST.get("id")
		entity = request.POST.getlist("entity[]")
		if entity and new_value:
			main_object = main_data.objects.filter(id=case_id).first()
			new_obj = PatientAskingFor(case_id=main_object, asking=new_value)
			new_obj.save()
			
			for ele in entity:
				key_obj = PatientAskingForKeyword(case_id=new_obj, keyword=keyword)
				key_obj.save()
			return Response({"response":"patient asking has been added!"})
		return Response({"response": "Bad Request"})

	def put(self, request):
		new_value = request.POST.get("intent")
		case_id = request.POST.get("id")
		entity = request.POST.getlist("entity[]")
		new_obj = None
		if new_value:
			logging.error(f"value -----> {new_value}")
			main_object = main_data.objects.filter(id=case_id).first()
			new_obj = PatientAskingFor.objects.filter(case_id=main_object).first()
			if new_obj:
				new_obj.asking = new_value
				new_obj.save()
			else:
				new_obj = PatientAskingFor(case_id=main_object, asking=new_value)
				new_obj.save()
		if entity:
			logging.error(f"entity -----> {entity}")
			entobjs = PatientAskingForKeyword.objects.filter(case_id=new_obj).all()
			old_asking = [ent.keyword for ent in entobjs]
			check = get_new_list_asking(old_asking, entity, entobjs, new_obj)
			if check:
				return Response({"response":"patient asking has been added!"})
		return Response({"response": "Bad Request"})

class HistoryApiView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		entity = request.POST.getlist("entity[]")
		case_id = request.POST.get("id")
		main_object = main_data.objects.filter(id=case_id).first()
		if entity:
			for ele in entity:
				foo1 = History(case_id=main_object, keyword=ele)
				foo1.save()
			return Response({"response":"history has been added!"})
		return Response({"response": "Bad Request"})

	def put(self, request):
		new_symptoms = request.POST.getlist("entity[]")
		case_id = request.POST.get("id")
		main_object = main_data.objects.filter(id=case_id).first()
		entobjs = History.objects.filter(case_id=main_object).all()
		old_symptoms = [ent.keyword for ent in entobjs]
		check = get_new_list_history(old_symptoms, new_symptoms, entobjs, main_object)
		if check:
			return Response({"response":"history has been updated!"})
		return Response({"response": "Bad Request"})

class EffectApiView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		entity = request.POST.getlist("entity[]")
		case_id = request.POST.get("id")
		main_object = main_data.objects.filter(id=case_id).first()
		if entity:
			for ele in entity:
				foo1 = Effect(case_id=main_object, keyword=ele)
				foo1.save()
			return Response({"response":"history has been added!"})
		return Response({"response": "Bad Request"})

	def put(self, request):
		new_symptoms = request.POST.getlist("entity[]")
		case_id = request.POST.get("id")
		main_object = main_data.objects.filter(id=case_id).first()
		entobjs = Effect.objects.filter(case_id=main_object).all()
		old_symptoms = [ent.keyword for ent in entobjs]
		check = get_new_list_effect(old_symptoms, new_symptoms, entobjs, main_object)
		if check:
			return Response({"response":"history has been updated!"})
		return Response({"response": "Bad Request"})

class MarkAsCompletedApiView(APIView):

	permission_classes = (IsAuthenticated,)

	def get(self, request):
		case_id = request.query_params.get("case_id")
		main_object = main_data.objects.filter(id=case_id).first()
		done_cases = CompletedCase(case_id=main_object)
		done_cases.save()
		return Response({"response":"case has been marked as completed!"})

class MarkAsInCompletedApiView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		case_id = request.query_params.get("case_id")
		logging.error(f"case id --> {case_id}")
		main_object = main_data.objects.filter(id=case_id).first()
		done_cases = CompletedCase.objects.filter(case_id=main_object).first()
		done_cases.delete()
		return Response({"response":"case has been marked as completed!"})


class RegisterApiView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		username = request.data.get("username")
		email = request.data.get("email")
		password = request.data.get("password")
		password = make_hash(password)
		user = create_user(username, email, password)
		if user:
			return Response({"msg":"user has created!!"})
		return {"msg":"Error"}


class MainDataApiView(generics.ListAPIView):
	
	queryset = main_data.objects.filter(title="Anxiety Disorders").all()
	serializer_class = MainData
	# permission_classes = [IsAdminUser]
	pagination_class = MyPagination

	
class LinkConfigApiView(generics.ListAPIView):
	
	queryset = LinkConfig.objects.filter(title="Anxiety Disorders").all()
	serializer_class = LinkConfigSerializer
	# permission_classes = [IsAdminUser]
	pagination_class = MyPagination


