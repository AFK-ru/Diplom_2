import allure
from api.base_client import BaseClient
from data.urls import CREATE_USER, LOGIN_USER, USER_DATA

class UserClient(BaseClient):
    
    @allure.step("Регистрация нового пользователя")
    def register_user(self, payload):

        return self.post(CREATE_USER, payload=payload)
    

    @allure.step("Авторизация пользователя с email: {email}")
    def login_user(self, email, password):

        payload = {"email": email, "password": password}

        return self.post(LOGIN_USER, payload=payload)


    @allure.step("Удаление пользователя по токену")
    def delete_user(self, token):

        headers = {"Authorization": token}

        return self.delete(USER_DATA, headers=headers)
