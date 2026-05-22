import requests
import allure

class BaseClient:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    @allure.step("Отправка POST запроса на {url}")
    def post(self, url, payload=None, headers=None):

        current_headers = {**self.headers, **(headers or {})}
        return requests.post(url, json=payload, headers=current_headers)

    @allure.step("Отправка GET запроса на {url}")
    def get(self, url, headers=None):

        current_headers = {**self.headers, **(headers or {})}
        return requests.get(url, headers=current_headers)

    @allure.step("Отправка DELETE запроса на {url}")
    def delete(self, url, headers=None):

        current_headers = {**self.headers, **(headers or {})}
        return requests.delete(url, headers=current_headers)
