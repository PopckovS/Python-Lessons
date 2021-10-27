Действия администратора
---
---

Находясь на странице админки, и просматривая группу обьектов некотрой 
модели, мы можем регистрировать «действия» - функции, которые вызываются
со списком объектов, выбранных на странице списка изменений.

**Функции действия**

Создать функцию действие можно как обычную функция и зарегистрировать ее
в модели в специальном атрибуте `actions`, описание для действия можно
присвоить в классовый атрибут этой функции `function_name.short_description`

```python
from django.contrib import admin
from myapp.models import Article

def actions_for_admin(modeladmin, request, queryset):
    print('Действие администратора, далее логика')

action_for_admin.short_description = 'Действие администратора'
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [actions_for_admin]

admin.site.register(Article, ArticleAdmin)
```

Все действия администратора будут доступны в выпадающем списке, рядом с
перечислением всех обьектов модели, как на рисунке.

По дефолтному поведению, действие администратора не сработает если 
не выбран хотябы один из эллементов модели.

![](img/admin_1.png)

---

Функция действие имеет 3 параметра :

1. `modeladmin` - какая модель какого приложения используется   
2. `request` - обьект запроса `WSGIRequest`
3. `queryset` - кверисет из выбранных обьектов

```
modeladmin =  bigdata.DestenyModelAdmin
request =  <WSGIRequest: POST '/admin/bigdata/destenymodel/'>
queryset =  <QuerySet [
                <DestenyModel: DestenyModel object (2)>, 
                <DestenyModel: DestenyModel object (1)>
            ]>
```

---
Действия как методы `ModelAdmin`
---

Действия можно регистрировать не как отдельную функцию, а как метод
класса.

Так же в место присвоения описания атрибуту класса этогой функции
дествия, можно использовать специальные декораторы 
`@admin.action(description='')` эти декораторы сработают ка кдля методов
класса так и для независимых функций действий

```python
from django.contrib import admin

class DestenyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    actions = ['action_for_admin']

    @admin.action(description='Новое действие администратора')
    def action_for_admin(self, request, queryset):
        print('self = ', self)
        print('request = ', request)
        print('queryset = ', queryset)

admin.site.register(DestenyModel, DestenyModelAdmin)
```
