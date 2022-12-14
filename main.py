import requests
import os.path

class work_yandex_disk:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path):
        """Метод загружает файл на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': name_file, "overwrite": "true"}
        response_get = requests.get(upload_url, params=params, headers=headers)

        if response_get.status_code == 200:
            print('Ссылка для загрузки файла на яндекс диск получена.')
        else:
            print(f'Ошибка получения ссылки. Код ошибки: {response_get.status_code}')
            return
        href = response_get.json()['href']

        response_put = requests.put(href, data=open(file_path, 'rb'))
        if response_put.status_code == 201:
            print('Успешно')
            return
        else:
            print(f"Ошибка загрузки! Код ошибки: {response_put.status_code}")
            return

if __name__ == '__main__':
    token = ''
    name_file = input('Укажите название файла с расширением, например, file.txt>>> ')
    path_file = os.path.abspath(name_file)
    print(path_file)
    uploader = work_yandex_disk(token)
    print(f'Начинается загрузка файла {name_file}.....')
    uploader.upload(path_file)



#

