Signals - сигналы
---
---

В Django присутствует такой механизм как `диспетчер сигналов`.
Сигналы оповещают о том что происходит некоторое событие в
некоторой части приложения.

Есть ряд типов сигналов:

>- **post_save**,  **pre_save** - происходит когда сохраняют
   > модель
> 
> 
>- **post_delete**, **pre_delete** - происходит когда удаляют
   > модель
> 
> 
>- **request_finished**, **request_started** - когда отправляют
   > HTTP запрос

Суть в том что мы регистрируем функцию, которая будет вызываться
автоматически при одном их произошедших событий.

---

Есть 2 способа которым можно зарегистрировать такие функции:

>1. Использовать `Signal.connect()` для регистрации функции.
> 
> 
>2. Использовать декоратор `receiver`

---




---


Пример сигнала срабатывающего после создания/обновления записи
в модели `ImagesModel`
В файле `models.py`
```python
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save, 
                                     pre_delete, 
                                     pre_save

@receiver(post_save, sender=ImagesModel)
def on_change_post(sender, instance, **kwargs):
    """Сигнал post_save - Создаем мини версию изображение"""
    if instance.big_image and os.path.isfile(instance.big_image.path):
        create_small_img(instance, size=500)

```





