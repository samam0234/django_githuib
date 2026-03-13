from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

# 여기에 view 함수를 작성합니다.
# 예 : 게시글 목록 보기, 게시글 작성 등
# 반드시 request(사용자가 보낸 요청정보를 담은 객체)를 첫번째  매개변수로 받아야 하고,
# 반드시 응답을(return)을 돌려줘야 한다.
# 예 : 게시글 목록 보기, 게시글 작성 등

# dummy
posts = {
        1: "첫 번째 게시글입니다.",
        2: "두 번째 게시글입니다.",
        3: "세 번째 게시글입니다.",
    }

def hello(request) :
    myInfo = {
        'name' : '둘리',
        'age' : 20,
        'addr' : '남극'
    }
    return render(request, 'board/hello.html', {'info' : myInfo})

# 문자열과 숫자 전달하기
def profile(request) :
    context = {
        'name' : '둘리',
        'age' : 20,
        'addr' : '남극'
    }
    return render(request, 'board/profile.html', context)

# 리스트로 전달하기
def fruits(request) :
    context = {
        'fruits_list' : ['사과', '바나나', '딸기', '포도']
    }
    return render(request, 'board/fruits.html', context)

def post_detail2(request) :
    context = {
        'post' : {
            'title' : '오늘 점심 메뉴', 
            'content' : '한식뷔페',
            'author' : '홍길동',
            'readCount' : 20
        }
    }

    return render(request, 'board/post_detail2.html', context)

# 여러 데이터 한꺼번에 전달하기
def blog_home(request):
    context = {
        'blog_name': '홍길동의 블로그',
        'post_count': 5,
        'is_owner': True,
        'recent_posts': [
            '첫 번째 게시글',
            '두 번째 게시글',
            '세 번째 게시글',
        ],
    }
    return render(request, 'board/blog_home.html', context)

def hello2(request) :
    myInfo = {
        'name' : '둘리',
        'age' : 20,
        'addr' : '남극'
    }
    return render(request, 'board/hello2.html', myInfo)

def post_list(request) :
    html = """
    <h1>게시판</h1>
    
    <p>서버 목록 확인 가능</p>
    <script>
        alert('!');
    </script>
    """
    return HttpResponse("this page is board page.", status=200, content_type="text/plain")

def board_list(request):
    posts = [
        {'id': 1, 'title': '장고 공부 시작!', 'author': '홍길동', 'date': '2025-01-01'},
        {'id': 2, 'title': 'Bootstrap 너무 편하다', 'author': '이순신', 'date': '2025-01-02'},
        {'id': 3, 'title': '템플릿 반복문 정복', 'author': '강감찬', 'date': '2025-01-03'},
    ]

    # posts = [

    # ]

    context = {
        'posts': posts,
    }
    return render(request, 'board/board_list.html', context)

def post_detail(request, pk) :
    # model단을 이용하여 데이터베이스의 게시글 테이블에서 pk번 글을 얻어와야 한다.
    
    if pk in posts :
        content = posts[pk]
        return HttpResponse(f"<h2>{pk}번 게시글</h2><p>{content}</p>")
    else :
        return HttpResponse(f"{pk}번 게시글은 존재하지 않습니다...")

def old_page(request) :
    return HttpResponseRedirect('/board/')

def home(request) :
    html = """
    <h1>MY Blog에 오신걸 환영합니다.</h1>
    <p>게시글 링크 : 
        <a href="http://127.0.0.1:8100/board">게시판 바로가기</a>
        <a href="http://127.0.0.1:8100/subquery">서브 게시판 바로가기</a>
    </p>
    """
    return HttpResponse(html)

def blog_list(request):
    context = {
        'posts': [
            {
                'title': 'Django 템플릿 필터 완전 정복하기',
                'content': 'Django 템플릿에서는 다양한 필터를 제공합니다. '
                           '필터를 잘 활용하면 View에서 데이터를 가공하지 않아도 '
                           '템플릿에서 원하는 형태로 출력할 수 있습니다.',
                'author': 'hong',
                'created_at': datetime(2024, 3, 1, 9, 0),
                'is_notice': True,
            },
            {
                'title': 'Bootstrap으로 예쁜 화면 만들기',
                'content': 'Bootstrap의 그리드 시스템을 활용하면 '
                           '반응형 웹 페이지를 쉽게 만들 수 있습니다.',
                'author': 'kim',
                'created_at': datetime(2024, 3, 2, 14, 30),
                'is_notice': False,
            },
        ]
    }
    return render(request, 'board/blog_list.html', context)

def subquery(request) :
    html = """
    <h1>여기는 보조 기능을 하는 페이지입니다.</h1>
    <div>
        선택가능한 기능
        <select id="select_btn">
            <option value=""></option>
            <option value="candy">사탕</option>
            <option value="snack">과자</option>
            <option value="dango">경단</option>
            <option value="been_milk">두유</option>
            <option value="yackkwa">약과</option>
            <option value="sugar_cookie">달고나</option>
        </select>
        <div id="result_value"></div>
    </div>
    """
    return HttpResponse(html)
