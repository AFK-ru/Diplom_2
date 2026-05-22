import pytest
import allure

@allure.title("Создание пользователя")
class TestCreateUser:

    @allure.step("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self, user_client, unique_user_data):

        response = user_client.register_user(unique_user_data)
        
        assert response.status_code == 200
        assert response.json().get("success") is True


    @allure.step("Ошибка при создании уже зарегистрированного пользователя")
    def test_create_duplicate_user_forbidden(self, user_client, created_user):

        existing_user_payload, _ = created_user
        response = user_client.register_user(existing_user_payload)
        
        assert response.status_code == 403
        assert response.json().get("message") == "User already exists"


    @allure.step("Ошибка при создании пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_forbidden(self, user_client, unique_user_data, missing_field):

        del unique_user_data[missing_field]
        response = user_client.register_user(unique_user_data)
        
        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"
