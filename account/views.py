import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Account

class AccountView(View):
	
	def post(self,request):
		data = json.loads(request.body)
		try:
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
			return JsonResponse({'message':'Account_DOES_NOT_EXIST'}, status=400)

