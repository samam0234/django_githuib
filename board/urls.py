from django.urls import path
# . 은 현재 폴더를 의미한다. board/views.py 파일을 가져와라 라는 의미
from . import views

# app_name = 'board'

urlpatterns = [
    # path('경로/', 실행할 함수의 위치, name='페이지의 별칭')
    path('', views.home, name='home'),    # 홈페이지
    path('board/', views.post_list, name='post_list'),    # 게시글 목록 페이지
    path('board/<int:pk>', views.post_detail, name='post_detail'),   # 게시글의 특정 글(게시글 상세보기)
    path('board/create', views.post_create, name='post_create') # 게시글 작성 페이지



    # path('hello/', views.hello),
    # path('hello2/', views.hello2),
    # path('profile/', views.profile),
    # path('fruits/', views.fruits),
    # path('post_detail2/', views.post_detail2),
    # path('home/', views.home),
    # path('blog_home/', views.blog_home),
    # path('blog_list/', views.blog_list),
    # path('board_list/', views.board_list),
    # path('base/', views.base),
    # path('old/', views.old_page),
    # path('subquery/', views.subquery)
]
