import allure

@allure.title("Авторизация пользователя")
class TestLoginUser:

    @allure.step("Успешный вход под существующим пользователем")
    def test_login_existing_user_success(self, user_client, created_user):

        user_payload, _ = created_user
        response = user_client.login_user(user_payload["email"], user_payload["password"])
        
        assert response.status_code == 200
        assert response.json().get("success") is True


    @allure.step("Ошибка авторизации с неверным логином и паролем")
    def test_login_with_incorrect_credentials_unauthorized(self, user_client):

        response = user_client.login_user("wrong_email_user_998@yandex.ru", "wrong_password_123")
        
        assert response.status_code == 401
        assert response.json().get("message") == "email or password are incorrect"
