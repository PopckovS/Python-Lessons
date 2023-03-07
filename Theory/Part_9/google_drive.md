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




