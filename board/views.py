from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from board.models import Post, Postview
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

# 여기에 view 함수를 작성합니다.
# 예 : 게시글 목록 보기, 게시글 작성 등
# 반드시 request(사용자가 보낸 요청정보를 담은 객체)를 첫번째  매개변수로 받아야 하고,
# 반드시 응답을(return)을 돌려줘야 한다.
# 예 : 게시글 목록 보기, 게시글 작성 등

# 여러 데이터 한꺼번에 전달하기
def home(request):

    return render(request, 'index.html')    # 홈 페이지


def post_list(request) :
    posts = Post.objects.all(); # 모든 게시글 목록 조회
    context = {
        'posts' : posts # context에 담기
    }
    return render(request, 'board/post_list.html', context)  # 템플릿으로 전달


def post_detail(request, pk) : 
    # get_object_or_404(Model, 조건)
    # post = get_object_or_404(Post, id=pk)     # pk번 글이 있으면 그 글의 데이터를 반환하고, 없으면 404
    # pk번 글이 있으면 그 글의 데이터를 반환하고,
    # 없으면 유저에게 에러메시지를 출력한뒤 '목록 페이지'로 이동하도록....
    post = Post.objects.filter(id=pk).first()   
    # filter는 없으면 None 반환, get() 없으면 예외발생(에러페이지)
    
    if post is None :   # 게시글이 없으면...
        output = """
        <script>
            alert('존재하지 않는 게시글 입니다!');
            location.href='/board/';
        </script>
"""

        return HttpResponse(output)

    # 게시글이 존재하면?
    # ip주소를 추출해옴
    
    ip_address = get_client_ip(request)

    # 해당 ip주소를 가진 사람이 해당 글을 24시간 이내에 조회한 기록이 없다 - 조회수증가, 조회기록저장
    # 해당 ip주소를 가진 사람이 해당 글을 24시간 이내에 조회한 기록이 있다 - 조회수증가X, 조회기록저장X
    
    # 24시간 전 시각 계산
    time_24h_ago = timezone.now() - datetime.timedelta(hours=24)
    
    already_viewed = Postview.objects.filter(
        post=post,
        ip_address=ip_address,
        viewed_at__gte=time_24h_ago
    ).exists()

    if not already_viewed : # 조회기록 없다 -> 조회수증가, 조회기록저장
        post.view_count += 1    # 해당 글의 조회수 1 증가
        post.save(update_fields=['view_count'])   # 해당 글(Post) update
        
        # PostView(조회수증가테이블)에 insert
        Postview.objects.create(post=post, ip_address=ip_address)   



    context = {
        'post' : post
    }
    # return render(request, 'board/post_detail.html', {'post' : Post.objects.get(id=pk)})
    return render(request, 'board/post_detail.html', context)

def get_client_ip(request) :
    """
        client_ip주소를 얻어오는 함수
    """
    # 프록시 서버를 거쳤을 때는 HTTP_X_FORWARDED_FOR 헤더에 ip주소가 담김
    http_x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if http_x_forwarded_for :
        ip = http_x_forwarded_for.split(',')[0].strip()
    else :
        ip = request.META.get("REMOTE_ADDR")
    return ip

def post_create(request) :
    """
        게시글 작성 버튼을 누르면 빈 폼이 있는 페이지가 응답되어야 하고,
        게시글 작성 후 "저장" 버튼을 누르면, 게시글이 db에 저장되고 업로드한 파일이 웹서버에 저장
        되어야 한다. (POST방식)
    """
    if request.method == 'POST' :
        # 텍스트 데이터(request.POST) + 업로드된 파일(request.FILES)
        form = PostForm(request.POST, request.FILES)

        if form.is_valid() :    # 데이터가 유효성 검증 후
            post = form.save()  # 문자열 데이터는 DB에, 파일 데이터는 media 폴더에 저장
            return redirect('post_list')

    else :  # GET
        form = PostForm()   # 비어있는 폼(form) 객체

    return render(request, 'board/post_form.html', {'form' : form})



# def hello(request) :
#     myInfo = {
#         'name' : '둘리',
#         'age' : 20,
#         'addr' : '남극'
#     }
#     return render(request, 'board/hello.html', {'info' : myInfo})

# # 문자열과 숫자 전달하기
# def profile(request) :
#     context = {
#         'name' : '둘리',
#         'age' : 20,
#         'addr' : '남극'
#     }
#     return render(request, 'board/profile.html', context)

# # 리스트로 전달하기
# def fruits(request) :
#     context = {
#         'fruits_list' : ['사과', '바나나', '딸기', '포도']
#     }
#     return render(request, 'board/fruits.html', context)

# def post_detail2(request) :
#     context = {
#         'post' : {
#             'title' : '오늘 점심 메뉴', 
#             'content' : '한식뷔페',
#             'author' : '홍길동',
#             'readCount' : 20
#         }
#     }

#     return render(request, 'board/post_detail2.html', context)


# def hello2(request) :
#     myInfo = {
#         'name' : '둘리',
#         'age' : 20,
#         'addr' : '남극'
#     }
#     return render(request, 'board/hello2.html', myInfo)

# def blog_home(request):
#     context = {
#         'blog_name': '홍길동의 블로그',
#         'post_count': 5,
#         'is_owner': True,
#         'recent_posts': [
#             '첫 번째 게시글',
#             '두 번째 게시글',
#             '세 번째 게시글',
#         ],
#     }
#     return render(request, 'blog_home.html', context)


# def board_list(request):
#     posts = [
#         {'id': 1, 'title': '장고 공부 시작!', 'author': '홍길동', 'date': '2025-01-01'},
#         {'id': 2, 'title': 'Bootstrap 너무 편하다', 'author': '이순신', 'date': '2025-01-02'},
#         {'id': 3, 'title': '템플릿 반복문 정복', 'author': '강감찬', 'date': '2025-01-03'},
#     ]

#     # posts = [

#     # ]

#     context = {
#         'posts': posts,
#     }
#     return render(request, 'board/board_list.html', context)



# def old_page(request) :
#     return HttpResponseRedirect('/board/')

# def home(request) :
#     html = """
#     <h1>MY Blog에 오신걸 환영합니다.</h1>
#     <p>게시글 링크 : 
#         <a href="http://127.0.0.1:8100/board">게시판 바로가기</a>
#         <a href="http://127.0.0.1:8100/subquery">서브 게시판 바로가기</a>
#     </p>
#     """
#     return HttpResponse(html)

# def blog_list(request):
#     context = {
#         'posts': [
#             {
#                 'title': 'Django 템플릿 필터 완전 정복하기',
#                 'content': 'Django 템플릿에서는 다양한 필터를 제공합니다. '
#                            '필터를 잘 활용하면 View에서 데이터를 가공하지 않아도 '
#                            '템플릿에서 원하는 형태로 출력할 수 있습니다.',
#                 'author': 'hong',
#                 'created_at': datetime(2024, 3, 1, 9, 0),
#                 'is_notice': True,
#             },
#             {
#                 'title': 'Bootstrap으로 예쁜 화면 만들기',
#                 'content': 'Bootstrap의 그리드 시스템을 활용하면 '
#                            '반응형 웹 페이지를 쉽게 만들 수 있습니다.',
#                 'author': 'kim',
#                 'created_at': datetime(2024, 3, 2, 14, 30),
#                 'is_notice': False,
#             },
#         ]
#     }
#     return render(request, 'board/blog_list.html', context)

# def subquery(request) :
#     html = """
#     <h1>여기는 보조 기능을 하는 페이지입니다.</h1>
#     <div>
#         선택가능한 기능
#         <select id="select_btn">
#             <option value=""></option>
#             <option value="candy">사탕</option>
#             <option value="snack">과자</option>
#             <option value="dango">경단</option>
#             <option value="been_milk">두유</option>
#             <option value="yackkwa">약과</option>
#             <option value="sugar_cookie">달고나</option>
#         </select>
#         <div id="result_value"></div>
#     </div>
#     """
#     return HttpResponse(html)
