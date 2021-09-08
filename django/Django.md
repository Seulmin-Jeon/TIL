# Django



- ### 준비


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

```python
mkdir templates
```

- templates 폴더 안에 base.html 만들기
- 프로젝트 파일 - settings.py - TEMPLATES 에서 'DIRS' : [BASE_DIR / 'templates'] 쓰기





- ### 시작


1. 앱 폴더 - models.py에서 클래스 생성, 변수(필드명) 쓰기

```python
+
def __ str __(self):
	return self.<변수명>
```



** models.py에 수정사항이 생기면 migrate 다시 하기

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```



서버 실행

```python
python manage.py runserver
```



2. 프로젝트 폴더 - urls.py

- import include 추가
- 앱 경로 설정

```python
path('<앱 이름>/', include('<앱 이름>.urls'))
```



3. 앱 폴더 - urls.py 파일 생성

- app_name 쓰기

```python
app_name = "<앱 이름>"
```

- 경로 설정

```python
from django.urls import path
from . import views
```

```python
urlpatterns = [
	path(''),
	path(),
	path(),
]
```



4. views.py에서 함수 작성

```python
import redirect
from .models import Article
from .forms import ArticleForm
```

```python
# 함수들 구조 잡아놓고 시작
def index():
    pass

def detail():
    pass

def create():
    pass

def update():
    pass

def delete():
    pass
```

+ 추가

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
```

```python
# GET 방식 (index, detail)
@require_safe

# GET + POST 방식 (create, udpate)
@require_http_methods(['GET', 'POST'])

# POST 방식 (delete)
@require_POST
```



5. templates 폴더 2개 생성

```
# 앱 폴더 내의 templates 폴더
index.html
detail.html
form.html
```

+

```
# 앱 폴더, 프로젝트 폴더와 같은 레벨에 templates 폴더
base.html
```



6. base. html

- ! + tab 해서 기본구조
- 부트스트랩 css, jagascript 파일 불러오기
- body에 `{% block content %}` `{% endblock content %}` 넣기!!



7. forms.py 생성

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = '__all__'
```







# <코드 예시>

```python
# urls.py
app_name = 'articles'

urlpatterns = [
    path(''. views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

```python
# models.py
class Article(models.Model):
    title = models.CharField(max_length= )
    content = models.TextField()
```

```python
# forms.py
class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = '__all__'
```



# views.py 함수 코드

### index

```python
def index(request):
    
    article = Article.object.all()
    
    context = {
        'articles': articles,
    }
    
    return render(request, 'articles/index.html', context)
```



### create

- new + create

```python
def create(request):
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
        
    context   = {
        'form': form,
    }
    
    return render(request, 'articles/index.html', context)
```



### update

- edit + update

```python
def update(request, pk):
    
    article = Article.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ArticleFor(request.POST, isntance=article)
        
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
        
    context = {
        'form': form,
    }
    
    return render(request, 'articles/update.html', context)
```



### delete

```python
def delete(request, pk):
    
    article = Article.objects.get(pk=pk)
    
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    
    else:
        return redirect('articles:detail', article.pk)
```







### cf. django-bootstrap-v5

![image-20210907102502627](Django.assets/image-20210907102502627.png)



```
pip freeze > requirements.txt
```



Add to INSTALLED_APPS in your `settings.py`:

> ```
> 'bootstrap5',
> ```





![image-20210907103109018](Django.assets/image-20210907103109018.png)



```
# base.html 최상단
{% load bootstrap5 %}
```

- 사용하려는 페이지마다 최상단에 추가(form.html)



```python
# form.html

{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
  {% if request.resolver_match.url_name == 'create' %}
    <h1>CREATE</h1>
  {% elif request.resolver_match.url_name == 'update' %}
     <h1>UPDATE</h1>
  {% endif %}

  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}

    <input type="submit">
  </form>
{% endblock content %}
```





![image-20210907104306474](Django.assets/image-20210907104306474.png)

```python
# 여러가지 옵션 추가 가능 (django-bootstrap-v5 공식페이지 참고)
ex.
{% bootstrap_form form layout='inline' %}
{% bootstrap_form form layout='horizontal' %}

{% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
```

