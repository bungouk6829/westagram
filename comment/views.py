import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Comment

class CommentView(View):

	def post(self,request):
		data = json.loads(request.body)
		try:
			Comment.objects.create(
				text = data['text']
			)
			return HttpResponse(status=200)
		except KeyError:
			return JsonResponse({'message':'INVALIDE_KEY'},status=400)

	def get(self,request):
		comment_data = list(Comment.objects.values())
		try:
			return JsonResponse({'data':comment_data},status=200)
		except Comment.DoesNotExist:
			return JsonResponse({'message':'COMMNET_DOST_NOT_EXIST'},status=400)
