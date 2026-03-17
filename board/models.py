from django.db import models

# 여기에 데이터 모델(테이블 구조)을 작성합니다.
# 예 : 게시글 모델, 댓글 모델 등

class Post(models.Model):
    """
    게시판 게시글 모델
    - 제목, 내용, 파일 첨부, 조회수, 공지 여부, 작성일, 수정일
    - 작성자(ForeignKey)는 25장에서 추가 예정
    """

    # ① 제목 (필수, 최대 200자)
    title = models.CharField(
        max_length=200,
        verbose_name='제목'
    )

    # ② 본문 (필수, 길이 제한 없음)
    content = models.TextField(
        verbose_name='내용'
    )

    # ③ 첨부파일 (선택, 모든 파일 형식 허용)
    attachment = models.FileField(
        upload_to='attachments/%Y/%m/',   # 연/월 폴더로 자동 분류
        blank=True,
        null=True,
        verbose_name='첨부파일'
    )

    # ④ 조회수 (기본값 0, 직접 입력하지 않음)
    view_count = models.IntegerField(
        default=0,
        verbose_name='조회수'
    )

    # ⑤ 공지 여부 (기본값 False)
    is_notice = models.BooleanField(
        default=False,
        verbose_name='공지'
    )

    # ⑥ 작성일시 (처음 저장될 때 자동 기록)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='작성일'
    )

    # ⑦ 수정일시 (저장될 때마다 자동 갱신)
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일'
    )

    def __str__(self):
        """Admin 페이지 등에서 게시글을 표시할 때 제목으로 보임"""
        return self.title

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '게시글 목록'
        ordering = ['-is_notice', '-created_at']
        # 공지글을 먼저, 그 다음 최신 순으로 정렬
