Google Drive
---

Google Drive (GD) - облачное хранилище, куда можно сохранять файлы, 
синхронизировать его с другими сервисами google.

---

Используем библиотеку

    pip install google-api-python-client

Для авторизации в GD, для начала создадим аккаунт в google, для аккаунта требуется
зарегистрировать приложение, для каждого из приложений можно создать сервисный 
аккаунт, от лица сервисного аккаунта и будем авторизоваться, при создании выдается 
специальный mail, который привязан именно к сервисному аккаунту, потребуется
сгенерировать специальный JSON файл с ключем. 

```python
import ee
from google.oauth2 import service_account
from googleapiclient.discovery import build

# файл JSON с секретным ключем для авторизации
GOOGLE_SERVICE_ACC_JSON_KEY = 'google_service_account_secret.json'

# специальный mail который выдается для сервисного аккаунта
GOOGLE_SERVICE_ACC = 'service-account-dzz1@ee-dzz1.iam.gserviceaccount.com'

# Указываем с каким сервисом соединяемся
GOOGLE_DRIVE = 'drive'

# Указываем версию API google drive
GOOGLE_DRIVE_VERSION = 'v3'

# Указываем права нашего клиента, даем все права на создание удаление чтение
GOOGLE_SCOPES = ['https://www.googleapis.com/auth/drive']

def google_drive_initial():
    """Initialize in service Google Drive"""
    
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_SERVICE_ACC_JSON_KEY, scopes=GOOGLE_SCOPES)
    service = build(
        GOOGLE_DRIVE, GOOGLE_DRIVE_VERSION, credentials=credentials)
    return service
```

---

Получение директории в drive по ее имени.

Метод `.files().list().execute()` дает возможность получить список файлов/директорий
из диска, параметр `q` указывает выражение поиска, специальный синтаксис
для фильтрации ресурсов с диска.

Найти ресурсы с что являются директориями 

    mimeType='application/vnd.google-apps.folder'

Отфильтровать ресурсы с названием `folder`

    and name='folder'

Объединяя фильтры можно

Параметр `fields` указывает какую информацию о найденном ресурсе 
вернуть, к примеру вернуть `id` ресурса, его название, и тип данных 

    fields="files(id, name, mimeType)"

Параметр `pageSize` указывает максимальное количество найденных 
ресурсов вернуть обратно.

Пример как получать ресурс по его имени на диске.

```python
def get_drive_folder(dir_name):
    """Get folder from Google Drive by name"""
    
    folder = service.files().list(
        q=f"mimeType='application/vnd.google-apps.folder' and name='{dir_name}'",
        fields="files(id, name, mimeType)",
        pageSize=1
    ).execute()
    return folder['files']
```

---

Создать директорию с указанным именем, создать ее как дочернею папку
указанной директории.

```python
def create_drive_folder(folder_name, parent_id=None):
    """Create folder in Google Drive"""
    
    folder = service.files().create(
        body={
            'mimeType': "application/vnd.google-apps.folder",
            'parents': [parent_id],
            'name': folder_name
        },
        fields="id"
    ).execute()
    folder['name'] = folder_name
    return folder
```

---

Скачать файл с Google Drive по указанному пути

```python
import io
from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO

def _load_file_from_google_drive(file_id, load_path):
    """Load file from Google Drive to storage"""

    try:
        request = service.files().get_media(fileId=file_id)

        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Скачано %d%%." % int(status.progress() * 100))

        # save file on storage
        with io.open(load_path, 'wb') as f:
            fh.seek(0)
            f.write(fh.read())

    except Exception as e:
        print('Ресурс скачан')
        return False
    return True
```

---

Получить все файлы определенного `mime` типа которые находятся внутри 
конкретной директории.

```python
def get_source_from_drive_folder(folder_id, mime):
    """Get list of source files from folder by id in Google Drive."""
    sources = service.files().list(
        q=f"mimeType='{mime}' and '{folder_id}' in parents",
        fields="nextPageToken, files(id, name, mimeType)",
        pageSize=1000 
    ).execute()
    return sources
```

---

При удалении из Google Drive директории через API, и получая список всех файлов
на Google Drive, можно увидеть что при удалении родитесльской директории, дочерние
эллементы не удалены, и присутствуют в списке получаемых файлов, при том что
если вы зайдете на сам Google Drive через браузер, то этих файлов не найдете.

При работе с Drive, рекомендую удалять рабочую директорию и все ее дочерние эллементы
при завершении работы.

```python
try:
    ...
except Exception as e:
    ...
else:
    ...
finally:
    for_delete = get_source_from_drive_folder(drive_folder_id)
    for file in for_delete["files"]:
        service.files().delete(fileId=file["id"]).execute()
    service.files().delete(fileId=drive_folder_id).execute()
```

---
Класс обертка для работы с Google Drive
---

Создадим удобный класс который бы предоставлял пользователю, удобный 
функционал для работы с Google drive, данный метод принимает название
рабочей директории на диске, в которой он будет удалять и создавать файлы,
и `drive_service` которое является классом типа `singlton` реализующее
подключение к диску.

Метод `load_from_google_drive_by_path` осуществляет скачивание всех файлов
определенного `MIME` типа из указанной директории с диска по локальному пути.

Внутренний метод `_load_file_from_google_drive` скачивает файл по указанному 
пути, и делает это чанками, небольшими кусочками которые по дефолту равняются
`100 MB` таким образом можно скачивать даже большие файлы, ибо скачивания
файлы по частям, оперативная память не будет забиваться.

```python
import logging
from googleapiclient.http import MediaIoBaseDownload
from pydantic import validate_arguments
from pathlib import Path


logger = logging.getLogger(__name__)


PAGE_SIZE = 100


class GoogleDriveFacade:
    def __init__(self, drive_service, work_dir: str):
        self.work_dir = work_dir
        self.drive_service = drive_service

    def _load_file_from_google_drive(self, request, load_file_path) -> bool:
        try:
            with open(load_file_path, "wb") as fd:
                downloader = MediaIoBaseDownload(fd, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
                    logger.info("Download %d%%."), int(status.progress() * 100)

        except Exception as e:
            logger.error("Error upload file %s", load_file_path)
            logger.exception(e)
            return False
        return True
    
    @validate_arguments
    def load_from_google_drive_by_path(self, dir_id: str, load_path: Path, mime_type: str) -> Path:
        """Download all files from Google Drive to local folder in tmp."""
        sources = self.get_all_from_drive_dir(dir_id, mime_type)

        for image in sources["files"]:
            file_path = load_path / image["name"]
            request = self.drive_service.files().get_media(fileId=image["id"])

            if self._load_file_from_google_drive(request, file_path):
                logger.info("Image successful upload by path: `%s` ", file_path)

        return load_path

    @validate_arguments
    def create_drive_dir(self, dir_name: str, parent_id: str) -> dict:
        """Create folder in Google Drive."""
        folder = self.drive_service.client.files().create(
            body={
                "mimeType": "application/vnd.google-apps.folder",
                "parents": [parent_id],
                "name": dir_name
            },
            fields="id"
        ).execute()
        folder["name"] = dir_name
        return folder

    @validate_arguments
    def get_drive_dir(self, dir_name: str) -> dict:
        """Get folder from Google Drive by name."""
        folder = self.drive_service.client.files().list(
            q="mimeType='application/vnd.google-apps.folder' and name='{name}'".format(name=dir_name),
            fields="files(id, name, mimeType)",
            pageSize=1
        ).execute()
        return folder["files"][0]

    @validate_arguments
    def get_all_from_drive_dir(self, dir_id: str, mime: str, page_size: int = PAGE_SIZE) -> dict:
        """Get list of source files from folder by id in Google Drive."""
        sources = self.drive_service.client.files().list(
            q="mimeType='{mime}' and '{id}' in parents".format(mime=mime, id=dir_id),
            fields="nextPageToken, files(id, name, mimeType)",
            pageSize=page_size
        ).execute()
        return sources

    @validate_arguments
    def delete_drive_dir(self, dir_id: str) -> None:
        """Clear Google Drive folder and delete."""
        files = self.get_all_from_drive_dir(dir_id)
        for file in files["files"]:
            self.drive_service.client.files().delete(fileId=file["id"]).execute()
        self.drive_service.client.files().delete(fileId=dir_id).execute()


__all__ = ["GoogleDriveFacade"]
```
