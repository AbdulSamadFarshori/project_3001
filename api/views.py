from django.shortcuts import render
from rest_framework import generics
from api.serializers import MainData 
from api.models import main_data, response, keywords, CompletedCase
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import status
from core.factory import authenticated

class GetDataFromBitIo(generics.ListAPIView):
	queryset = main_data.objects.all()
	serializer_class = MainData

	def list(self, request):
		anxiety_queryset = main_data.objects.filter(heading="Anxiety Disorders")[:1000]
		depression_queryset = main_data.objects.filter(heading="Depression")[:1000]
		queryset = [*anxiety_queryset, *depression_queryset]
		serializer = MainData(queryset, many=True)
		return Response(serializer.data)

class LoginView(APIView):
	
	def post(self, request):
		user = request.POST.get("username")
		password = request.POST.get("password")
		if authenticated(user, password):
			return Response({"msg":True, "name":user})
		return Response({"msg":False})

class FormSubmitView(APIView):

	def post(self, request):
		username = request.POST.get("username")
		keyword = request.POST.getlist("keyword[]")
		score = int(request.POST.get("score"))
		summary = request.POST.get("summary")
		reply = request.POST.get("reply")
		case_id = int(request.POST.get("case_id"))
		main_object = main_data.objects.filter(id=case_id).first()
		if reply and summary:
			response_object = response(
								case_id=main_object, 
								counsellor=username, 
								relavent_score=score, 
								summary=summary, 
								reply=reply
								)
			response_object.save()
			for tag in keyword:
				keyword_object = keywords(case_id=main_object, keyword=tag)
				keyword_object.save()
			done_object = CompletedCase(case_id=main_object)
			done_object.save()
			return Response({"response":True})

		return Response({"response":False})


