from django import forms
from .models import Post

class PostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields = ['title', 'content', 'attachment', 'image']

        # 한국어 라벨 설정
        labels = {
            'title' : '제목',
            'content' : '내용',
            'attachment' : '첨부파일',
            'image' : '첨부 이미지'
        }

        # 각 필드마다 위젯 설정
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '제목을 입력하세요...'
            })
        }