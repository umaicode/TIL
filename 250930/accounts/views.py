from django.shortcuts import render


# Create your views here.
# auth는 Model Form을 안쓴다.
# built-in form을 쓴다.
from django.contrib.auth.forms import AuthenticationForm  # 로그인을 위한 폼

from django.contrib.auth import login as auth_login


def login(request):
    pass
