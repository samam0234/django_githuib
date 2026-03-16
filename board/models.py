from django.db import models

# 여기에 데이터 모델(테이블 구조)을 작성합니다.
# 예 : 게시글 모델, 댓글 모델 등

class Post(models.Model) :
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):  # toString() : 디버깅을 편리하게 하기 위해 객체를 출력하면
        return self.title   # 객체주소가 아닌 게시글의 제목이 출력되도록.