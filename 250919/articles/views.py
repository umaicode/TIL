from django.shortcuts import render


# Create your views here.
def index(request):
    # context는 딕셔너리 구조
    # templates에서 index.html
    # {{ name }} ---> context의 key 값을 통해서 value를 가져온다.
    context = {"name": "Jane", "number": 1}

    return render(request, "articles/index.html", context)


import random


def dinner(request):
    foods = ["족발", "보쌈", "치킨", "피자"]
    picked = random.choice(foods)
    context = {
        "foods": foods,
        "picked": picked,
    }

    return render(request, "articles/dinner.html", context)


def search(request):
    return render(request, "articles/search.html")


def throw(request):
    return render(request, "articles/throw.html")


def catch(request):
    # throw에서 보낸 값은 request에 담겨있다.
    # throw: form태그에서 name으로 넘겨준 것.
    # text = request.GET['message']
    # GET : GET 방식의 GET
    # get : 딕셔너리 메서드
    text = request.GET.get("throw")

    context = {
        "text": text,
    }

    return render(request, "articles/catch.html", context)
    # 1. context 없이 리턴하는 방법
    # return render(request, "articles/catch.html", {"text": text})


# number는 앱의 urls.py로부터 넘어온 것
def detail(request, number):

    context = {"number": number}

    return render(request, "articles/detail.html", context)
