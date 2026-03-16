from django.db import models

# 여기에 데이터 모델(테이블 구조)을 작성합니다.
# 예 : 게시글 모델, 댓글 모델 등

class Post(models.Model) :
    # 제목 : 짧은 문자열, 최대 200자
    title = models.CharField(max_length=200)
    # 내용 : 여러줄 텍스트
    content = models.TextField()

# ③ 첨부 파일: 선택 첨부 (없어도 됨)
    attachment = models.FileField(
        upload_to='attachments/',  # MEDIA_ROOT/attachments/ 에 저장
        blank=True,                # 폼에서 비워둬도 됨
        null=True                  # DB에 NULL 허용
    )

    # ④ 조회수: 정수, 기본값 0
    view_count = models.IntegerField(default=0)

    # ⑤ 작성일: 처음 저장될 때 자동 기록
    created_at = models.DateTimeField(auto_now_add=True)

    # ⑥ 수정일: 저장될 때마다 자동 갱신
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # toString() : 디버깅을 편리하게 하기 위해 객체를 출력하면
        return self.title   # 객체주소가 아닌 게시글의 제목이 출력되도록.
    
    class Meta:
        ordering = ['-created_at']  # 최신 글이 위에 오도록 정렬(내림차순 정렬)