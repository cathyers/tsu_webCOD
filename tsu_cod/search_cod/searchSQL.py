from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.views.decorators import csrf
from codOpt.models import Data

# 接收POST请求数据
def search_post(request):
	template_name = 'search_cod/searchSQL.html'
	ctx ={}
	#ctx.update(csrf(request))
	#if request.POST:
	if request.method == "POST": 
		# message = '你搜索的内容为: ' 
		# ctx['rlt'] = 'The COD id you need is: '+ request.POST['q']
		codFile =int(float(request.POST['q']))
		codData = Data.objects.get(file=codFile)
		ctx['journal'] = 'The journal is: ' + codData.journal
		ctx['title'] = 'The title is: ' + codData.title
		ctx['a'] = 'The a is: ' + str(codData.a)
		ctx['b'] = 'The b is: ' + str(codData.b)
		ctx['c'] = 'The c is: ' + str(codData.c)
		ctx['alpha'] = 'The alpha is: ' + str(codData.alpha)
		ctx['beta'] = 'The beta is: ' + str(codData.beta)
		ctx['gamma'] = 'The gamma is: ' + str(codData.gamma)
	return render(request, "search_cod/searchSQL.html", ctx)
	#return HttpResponse(message)


# def search_post(request):
#     return HttpResponse("Hello, world. You're at the polls index.")