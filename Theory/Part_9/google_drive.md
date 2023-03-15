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
    """
    Initialize in service Google Drive
    """
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
    """
    Get folder from Google Drive by name
    """
    folder = service.files().list(
        q=f"mimeType='application/vnd.google-apps.folder' and name='{dir_name}'",
        fields="files(id, name, mimeType)",
        pageSize=1
    ).execute()
    return folder['files']
```

