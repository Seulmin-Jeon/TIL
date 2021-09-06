```python
# urls.py
app_name = 'articles'

urlpatterns = [
    path(''. views.index, name='index'),
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

