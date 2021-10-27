Действия администратора
---
---

Находясь на странице админки, и просматривая группу обьектов некотрой 
модели, мы можем регистрировать «действия» - функции, которые вызываются
со списком объектов, выбранных на странице списка изменений.


**Функции действия**

```python
from django.contrib import admin
from myapp.models import Article

@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]

admin.site.register(Article, ArticleAdmin)
```
