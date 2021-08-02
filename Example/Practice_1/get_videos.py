import os
import youtube_dl

"""
Данная программа скачивает видео с Youtube и сохраняет в формате mp3

URL для видео должно быть в формате 'https://www.youtube.com/watch?v=p4KwdJdCy0o'
Обратите внимание что если в URL есть параметр '&list=' ио будет скачан весь
плей лист.
"""

links = [
    "https://www.youtube.com/watch?v=p4KwdJdCy0o",
]


def uploader(links: list):

    "В цикле скачивает все видео с Youtube"

    ydl_opts = {
        # 'outtmpl': "", # Директория для скачивания
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            # 'preferredcodec': 'wav', # Формат в котором будет скачено видео
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        # 'keepvideo': True # даляет или оставляет оригинал видео
        'keepvideo': False
    }

    for video in links:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video])


if __name__ == "__main__":
    uploader(links)
