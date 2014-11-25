from django.shortcuts import (render_to_response, render)
from django.http import HttpResponse

	#return HttpResponse("Hello, World!")
# Create your views here.
def index(request):
	return render(request, 'scholar_survey_app/index.html', {
		'message': 'This is Scholar Survey.',
		})
