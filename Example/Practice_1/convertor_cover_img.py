from PIL import Image

"""
Модуль для стилизации изображений. 

add_alpha_canal - Добавляет изображению прозрачность в указанном
размере, оот 0 до 256  

convert_jpg_to_png - Конвертирует изображение из .jpg в .png
и сохраняет его в том же файле 

create_combine_image - Накладывает изображение с Альфа каналом 
на обычное изображение.

Пример использования:
    add_alpha_canal('2.png', 'Filter-1.png', 128)
    convert_jpg_to_png('123.jpg', 'Photo-1.png')
    create_combine_image('Photo-1.png', 'Filter-1.png', 'Combine-1.png')
"""


def convert_jpg_to_png(photo_jpg):
    """
    Конвертирует изображение из jpg в png
    Возвращаем новый путь к картинке.
    """
    img = Image.open(photo_jpg)
    photo_png = photo_jpg.replace('.jpg', '.png')
    img.save(photo_png)
    return photo_png


def add_alpha_canal(source_png, alpha_value=128):
    """Добавляет png изображению, Альфа канал."""
    img = Image.open(source_png)
    img.putalpha(alpha_value)
    img.save(source_png)


def create_combine_image(photo_png, filter_png, result_img):
    """
    Наложение фильтра на изображение.

    Изменяет размер фильтра, подстраивая его под
    изображение, накладывает фильтр на изображение.

    photo_png - изображение без прозрачности
    filter_png - изображение с прозрачностью
    """
    # Открываем изображение
    background = Image.open(photo_png)
    foreground = Image.open(filter_png)

    # Получаем их размеры
    back_width, back_height = background.size

    # Подстраиваем фильтр под изображение
    foreground = foreground.resize((back_width, back_height))

    # Накладываем фильтр на фото и сохраняем
    background.paste(foreground, (0, 0), foreground)
    background.save(result_img)
