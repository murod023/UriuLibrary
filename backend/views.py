from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import *

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods



from django.http import HttpResponseRedirect

@login_required
def index(request):
    context = dict()
    if request.user.groups.filter(name='Склад').exists():
        return render(request, 'index-1.html', context)
    else:
        # Если пользователь не входит ни в одну из этих групп
        return render(request, '404.html', context)