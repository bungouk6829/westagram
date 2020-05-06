import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Account

class AccountView(View):
	
	def post(self,request):
		data = json.loads(request.body)
		try:
			if Account.objects.filter(email=data['email']):
				return JsonResponse({'message':'EMAIL_ALREADY_EXIST'}, status=400)
			else:
				Account.objects.create(
					name = data['name'],
					phone_number = data['phone_number'],
					email = data['email'],
					password = data['password']
				)
				return HttpResponse(status=200)

		except KeyError:
			return JsonResponse({'message':'INVALIDE_KEY'}, status=400)
	def get(self,request):
		account_data = list(Account.objects.values())
		try :
			return JsonResponse({'data':account_data}, status=200)
		except Account.DoesNotExist:
			return JsonResponse({'message':'ACCOUNT_DOES_NOT_EXIST'}, status=400)

class SignUpView(View):
	
	def post(self,request):
		data = json.loads(request.body)
		try:
			user_email =data['email']
			user_password = data['password']
			if Account.objects.filter(email=user_email):
				user = Account.objects.filter(email=user_email).first()
				if user.password == user_password:
					return HttpResponse(status=200)
				else:
					return JsonResponse({'message':'INVALIDE_PASSWORD'}, status=400)
			else:
				return JsonResponse({'message':'EMAIL_NOT_FOUND'}, status=400)
		except KeyError:
			return JsonResponse({'message':'INVALIDE_KEY'}, status=400)
