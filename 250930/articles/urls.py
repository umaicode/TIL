from django.contrib import admin
from django.urls import path

from . import views

# url naming pattern
app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    # variable routing
    # pk의 변수에 할당된 값은 views.py의 detail함수의 pk 매개변수로
    path("<int:pk>/", views.detail, name="detail"),
    # 1. 기존 방식 : 렌더링, 리다이렉트 분리
    # # 게시글 생성 페이지를 단순히 렌더링 하는 역할
    # path("new/", views.new, name="new"),
    # 클라이언트에서 입력한 데이터를 DB에 저장
    path("create/", views.create, name="create"),
    # 단일 게시글 조회 후 삭제
    path("<int:pk>/delete/", views.delete, name="delete"),
    # 1. 기존 방식 : edit 사용
    # # 페이지 렌더링
    # path("<int:pk>/edit/", views.edit, name="edit"),
    # 페이지 리다이렉트
    path("<int:pk>/update/", views.update, name="update"),
]
