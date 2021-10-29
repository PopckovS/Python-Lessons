ModelAdmin
---

За все работу с административнйо панелью в `Django` отвечает класс 
следующая иерархия вложенности классо:

1. `BaseModelAdmin` - базовый класс для всей административной части.

2. `ModelAdmin(BaseModelAdmin)` - класс более высокого уровня, является
основным классом с которым происходит вся работа, от него и администрируем
все модели для взаимодействия с ней в админке.

3. `InlineModelAdmin(BaseModelAdmin)`

---
Действия администратора
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

---
URL в админке `ModelAdmin.get_urls()`
---

`get_urls` - Метод возвращает `URL` адреса которые будут использовать
для взаимодействия с этой зарегистрированной моделью.

Используя этот метод мы можем расширять административную часть, добавляя
представления и `URL` для них, тут можно как зарегистрировать новое 
представлние для административной части, так и для создания представления
которое не будет иметь отображения, а будет отрабатывать на кастомно 
созданную кнопку.

---

Для регистрации нового пути, наследуем `super().get_urls()` родительский
метод, и расширяем его дополнительным путем, регистрируем его так же как
и обычные пути в `settings`

Так же создаем представление `my_view` в административной части, которое
и регистрируем за указанным `URL`, определяем для него контекст и шаблон 
для внешнего вида.

```python
from .models import DestenyModel
from django.template.response import TemplateResponse
from django.urls import path

class DestenyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    
    def get_urls(self):
        """Расширяем пути, добавляя виды для конкретно этой админки"""
        # получаем родительские URL
        urls = super().get_urls()

        # создаем пути для конкретно этой админки
        my_urls = [
            path('my_view/', self.my_view),
        ]

        # соединяем пути и возвращаем их
        return my_urls + urls

    def my_view(self, request):
        """Новое представление для админки"""
        context = {'var_1': 1, 'var_2': 2,}
        return TemplateResponse(request, "sometemplate.html", context)

admin.site.register(DestenyModel, DestenyModelAdmin)
```


```python
   def get_urls(self):
        urls = super(DestinyModelAdmin, self).get_urls()
        custom_urls = [url('^heatmap/$', self.process_heatmap, name='heatmap'), ]
        return custom_urls + urls
```
