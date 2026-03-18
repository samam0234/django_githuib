from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta : #! 반드시 필요
        model = Post
        fields=['title', 'content', 'attachment', 'image']
        
        # 한국어 라벨 설정
        labels = {
            'title' : '제목',
            'content' : '본문', 
            'attachment' : '첨부파일',
            'image' : '첨부 이미지'
        }
        
        # 각 필드마다 위젯 설정
        widgets = {
# 제목: 한 줄 텍스트 입력칸
            'title': forms.TextInput(attrs={
                'class':       'form-control',        # Bootstrap 입력 스타일
                'placeholder': '제목을 입력하세요',   # 입력칸 안 안내 문구
            }),

            # 내용: 여러 줄 텍스트 입력칸
            'content': forms.Textarea(attrs={
                'class':       'form-control',        # Bootstrap 입력 스타일
                'placeholder': '내용을 입력하세요',   # 입력칸 안 안내 문구
                'rows':        10,                    # 세로 높이 (10줄)
            }),

            # 이미지: 파일 업로드 입력칸 (이미지 전용)
            # ClearableFileInput: 수정 시 기존 파일 삭제 기능 포함
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',  # Bootstrap 파일 입력 스타일
            }),

            # 첨부파일: 파일 업로드 입력칸 (모든 파일 허용)
            'attachment': forms.ClearableFileInput(attrs={
                'class': 'form-control',  # Bootstrap 파일 입력 스타일
            }),
        }