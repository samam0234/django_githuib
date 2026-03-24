# Dockerfile

# Python 3.12 slim 버전을 기반 이미지로 사용
# slim: 불필요한 파일을 제거한 가벼운 리눅스 환경
FROM python:3.12-slim

# 컨테이너 안에서 작업할 디렉토리 설정
WORKDIR /app

# MariaDB/MySQL 클라이언트 라이브러리 설치
# mysqlclient 파이썬 패키지가 이것을 필요로 합니다
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 먼저 복사 → pip install
# 소스코드가 바뀌어도 requirements.txt가 같으면 이 단계 캐시 재사용 → 빌드 빠름
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn 설치 (배포용 Python 웹 서버 — runserver 대체)
RUN pip install gunicorn

# 프로젝트 전체 파일 복사
COPY . .

# 정적 파일을 staticfiles/ 폴더에 모으기
# Nginx가 이 폴더를 직접 서빙합니다
# RUN python manage.py collectstatic --noinput

# 8000번 포트 사용 명시
EXPOSE 8000

# 컨테이너 시작 시 Gunicorn으로 Django 실행
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]