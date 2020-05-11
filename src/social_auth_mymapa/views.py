from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
  head_text = 'Index page'
  template = 'index.pug'
  return render(request, template, {
    'head_text': head_text,
  })


def login(request):
  head_text = 'Login'
  template = 'login.pug'

  return render(request, template, {
    'head_text': head_text
  })