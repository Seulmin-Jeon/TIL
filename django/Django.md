# Django



### 준비

​	(파일 생성 후 파일로 들어감)

```
mkdir <파일 이름>
cd <파일 이름>
```



1. 가상환경 설정 및 활성화

```
python -m venv venv
source venv/Scripts/activate
```



2. README 파일, .gitignore 파일 생성

```
touch README.md .gitignore
```

- gitignore.io 에서 windows, macos, django, visualstudiocode, python 쓰고 .gitignore 파일에 붙여넣기



2. 장고 설치

```
pip install django
또는
pip install django django_extensions
```

+

```
pip freeze > requirements.txt
```





3. 프로젝트 파일 생성

```
django-admin startproject <프로젝트 이름> .
```

-  . 빼먹지 말기



4. 앱 생성 및 앱 등록

```
python manage.py startapp <앱 이름>
```

- 프로젝트 파일 - settings.py - INSTALLED_APPS 에서 앱 등록



5. base.html 만들기

```
mkdir templates
```

- templates 폴더 안에 base.html 만들기
- 프로젝트 파일 - settings.py - TEMPLATES 에서 'DIRS' : [BASE_DIR / 'templates'] 쓰기





### 시작

1.  앱 폴더 - models.py에서 클래스 생성, 변수(필드명) 쓰기

   ```
   +
   def __ str __(self):
   	return self.<변수명>
   ```

   

   ** models.py에 수정사항이 생기면 migrate 다시 하기

```
python manage.py makemigrations
```

```
python manage.py migrate
```



2. 프로젝트 폴더 - urls.py

- import include 추가
- 앱 경로 설정

```
path('<앱 이름>/', include('<앱 이름>/urls'))
```



3. 앱 폴더 - urls.py 파일 생성

- app_name 쓰기

```
app_name = "<앱 이름>"
```

- 경로 설정

```
from django.urls import path
from . import views
```

```
urlpatterns = [
	path(''),
	path(),
	path(),
]
```



4. 

