from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required

from .models import User


class Login(View):
  def post(self, request):

    email = request.POST.get('email')
    username = request.POST.get('username')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')

    user = authenticate(email=email,
                        password=password)
    if user:
      response = {
        'status': 'error',
        'message': 'user already exists, please log in'
      }
    else:
      user = User.objects.create_user(
        email=email,
        username=username,
        last_name=last_name,
        password=password
      )
      response = {
        'status': 'success'
      }
      login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return HttpResponse(json.dumps(response))

  def get(self, request):
    head_text = 'Login'
    template = 'login.pug'

    return render(request, template, {
      'head_text': head_text
    })


def login_view(request):
  pass

@login_required
def Logout(request):
  logout(request)
  return redirect('login')
