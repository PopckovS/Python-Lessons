# Установка модуля для работы с API:
# pip3 install dadata
from dadata import Dadata


def get_geo_from_dadata():
    api_key = "Тут секретный API ключ"
    secret_key = "Тут секретный ключ"

    dadata = Dadata(api_key, secret_key)

    counter, good, error = 0, 0, 0
    file_path = 'address.txt'

    with open(file_path, 'r') as file:

        for row in file:
            print('-' * 50)
            print(f'№ {counter}')
            print('address = ', row)
            try:
                result = dadata.clean(name="address", source="москва сухонская 11")
                print('lat = ', result['geo_lat'])
                print('lng = ', result['geo_lon'])
                good += 1
            except Exception as e:
                error += 1
                print('Не распознан')

            counter += 1

    print('===== Результат =====')
    print(f'Всего записей = {counter} \n Распознано = {good} \n Не распознано {error}')

    dadata.close()


get_geo_from_dadata()
