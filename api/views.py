from django.shortcuts import render
from rest_framework import generics
from api.serializers import MainData 
from api.models import main_data
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
		user = request()
		password = request.POST.get("password")
		print(request.POST)
		print(user, password)
		if authenticated(user, password):
			return Response({"msg":True, "name":user})
		return Response({"msg":False})
