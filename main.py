'Скрипт для создания красивых постеров для фильмов'

from io import BytesIO

import requests
from loguru import logger
from PIL import Image, ImageDraw, ImageFont


# Данные о фильме
TITLE = "FIGHT CLUB"
YEAR = "1999"
DURATION = "139"
DIRECTED_BY = "DAVID FINCHER"
PRODUCED_BY = "ART LINSON  CEAN CHAFFIN"
STARRING = "BRAD PITT  EDWARD NORTON  HELENA BONHAM CARTER"

IMAGE_URL = "https://i.pinimg.com/736x/dc/25/24/dc25246cb3efeb5819b8e60602656f04.jpg"


# Константы
FONT_TITLE = "res/font-title.ttf"
FONT_TEXT = "res/font-text.ttf"

TEXT_COLOR = '#2f2b28'
BG_COLOR = '#dcd9d2'

OUTPUT_NAME = 'output.png'


def crop_to_square(image):
    'Функция для обрезки изображения под квадрат'

    width, height = image.size
    min_dim = min(width, height)
    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    right = (width + min_dim) // 2
    bottom = (height + min_dim) // 2
    return image.crop((left, top, right, bottom))


def main():
    'Основная функция запуска скрипта'

    # Загрузка изображения
    response = requests.get(IMAGE_URL, timeout=20)
    img = Image.open(BytesIO(response.content))

    # Обрезаем изображение под квадрат
    img = crop_to_square(img)

    # Создаем новый постер
    poster_width = 574
    poster_height = 857
    poster = Image.new('RGB', (poster_width, poster_height), BG_COLOR)

    # Изменяем размер изображения и добавляем отступы
    img = img.resize((poster_width - 60, poster_width - 40))
    poster.paste(img, (30, 42))

    # Создаем объект для рисования
    draw = ImageDraw.Draw(poster)

    # Загружаем шрифты
    title_font = ImageFont.truetype(FONT_TITLE, 56)
    text_font = ImageFont.truetype(FONT_TEXT, 20)

    # Определяем начальную позицию для текста
    text_start_y = img.height + 30  # 20 пикселей отступа под изображением

    # Рисуем текст на постере
    draw.text(
        (30, text_start_y),
        TITLE.upper(),
        font=title_font,
        fill=TEXT_COLOR
    )

    draw.text(
        (30, text_start_y + 80),
        YEAR, font=text_font,
        fill=TEXT_COLOR
    )

    draw.text(
        (30, text_start_y + 120),
        f"running time   {DURATION} MINUTES",
        font=text_font,
        fill=TEXT_COLOR
    )

    draw.text(
        (30, text_start_y + 150),
        f"directed by   {DIRECTED_BY}",
        font=text_font,
        fill=TEXT_COLOR
    )

    draw.text(
        (30, text_start_y + 180),
        f"produced by   {PRODUCED_BY}",
        font=text_font,
        fill=TEXT_COLOR
    )

    draw.text(
        (30, text_start_y + 220),
        f"starring   {STARRING}",
        font=text_font,
        fill=TEXT_COLOR
    )

    # Сохраняем постер
    poster.save(OUTPUT_NAME)
    logger.info('Постер сохранён в {}', OUTPUT_NAME)


if __name__ == '__main__':
    main()
