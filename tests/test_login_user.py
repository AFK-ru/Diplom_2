import allure
from data.expected_messages import INCORRECT_CREDENTIALS_MSG
from data.user_data import INVALID_EMAIL, INVALID_PASSWORD

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

        response = user_client.login_user(INVALID_EMAIL, INVALID_PASSWORD)
        
        assert response.status_code == 401
        assert response.json().get("message") == INCORRECT_CREDENTIALS_MSG
