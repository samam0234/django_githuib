from django.contrib import admin
from .models import Post

# 여기에 관리자 페이지에 표시할 모델을 등록합니다.
admin.site.register(Post)   # Admin페이지에서 Post 모델을 관리하도록 등록

