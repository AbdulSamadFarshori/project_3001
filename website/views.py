from django.shortcuts import render
from api.models import CompletedCase
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import get_user_model
from core.factory import user_is_valid
from django.shortcuts import redirect

class HomeView(TemplateView):
	template_name = "website/index.html"

class LoginView(TemplateView):
	template_name = "website/login.html"

class MainView(View):

	template_name = 'website/cases.html'
	
	def get(self, request, var):
		done_list = [i.case_id.id for i in CompletedCase.objects.all()]
		status = user_is_valid(var)
		if status:
			return render(request, self.template_name, {"context":var, "done_list":done_list})
		return redirect("login")



