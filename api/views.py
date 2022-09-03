from django.shortcuts import render
from rest_framework import generics
from api.serializers import (MainData, 
							ReplyDataSerializer, 
							ReplyThreadSerializer, 
							LinkConfigSerializer
							) 
from api.models import (main_data, ReplyData, 
						response, ReplyThread,
						keywords, 
						CompletedCase,
						LinkConfig, 
						EntityData, 
						IntentData) 
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination_veiw import MyPagination
from django.contrib.auth import get_user_model
from rest_framework import status
from core.factory import authenticated, create_hash_key, make_hash, create_user
from website.models import Cookies
import logging

class LoginView(APIView):
	
	def post(self, request):
		user = request.POST.get("username")
		password = request.POST.get("password")
		if authenticated(user, password):
			cookies = Cookies.objects.filter(id=1).first()
			if cookies:
				return Response({"msg":True, "name":user, "cookies":cookies.set_cookies})
			else:
				cookies_key = create_hash_key()
				obj = Cookies(set_cookies=cookies_key)
				obj.save()
				print(obj.set_cookies)
				return Response({"msg":True, "name":user, "cookies":obj.set_cookies})
		return Response({"msg":False})

class FormSubmitView(APIView):

	def post(self, request):
		username = request.POST.get("username")
		asking = request.POST.get("asking")
		need = request.POST.get("need")
		keyword = request.POST.getlist("keyword[]")
		score = int(request.POST.get("score"))
		summary = request.POST.get("summary")
		reply = request.POST.get("reply")
		case_id = int(request.POST.get("case_id"))
		main_object = main_data.objects.filter(id=case_id).first()
		if reply and summary:
			response_object = response(
								case_id=main_object, 
								counselor=username,
								patient_asking=asking,
								patient_need=need, 
								relavent_score=score, 
								summary=summary, 
								reply=reply
								)
			response_object.save()
			for tag in keyword:
				keyword_object = keywords(case_id=main_object, keyword=tag.lower())
				keyword_object.save()
			done_object = CompletedCase(case_id=main_object)
			done_object.save()
			return Response({"response":True})

		return Response({"response":False})

class RegisterApiView(APIView):

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


