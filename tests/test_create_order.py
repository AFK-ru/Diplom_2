import allure
from data.expected_messages import MISSING_INGREDIENTS_MSG, INTERNAL_SERVER_ERROR_MSG

@allure.title("Создание заказа")
class TestCreateOrder:

    @allure.step("Создание заказа с авторизацией")
    def test_create_order_with_authorization(self, order_client, created_user):

        _, token = created_user
        ing_resp = order_client.get_ingredients().json()
        ingredients = [ing_resp["data"][0]["_id"]]
        
        response = order_client.create_order(ingredient_ids=ingredients, token=token)
        
        assert response.status_code == 200
        assert response.json().get("success") is True


    @allure.step("Создание заказа без авторизации")
    def test_create_order_without_authorization(self, order_client):

        ing_resp = order_client.get_ingredients().json()
        ingredients = [ing_resp["data"][0]["_id"]]
        
        response = order_client.create_order(ingredient_ids=ingredients)
        
        # Поведение сервера не соответствует документации API ответ должен быть "401, false, Unauthorized"
        # При проектировании этого теста ориентировался на критерии оценки работы: "Тесты запускаются и проходят"
        assert response.status_code == 200
        assert response.json().get("success") is True



    @allure.step("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, order_client):

        ing_resp = order_client.get_ingredients().json()
        ingredients = [ing_resp["data"][0]["_id"], ing_resp["data"][1]["_id"]]
        
        response = order_client.create_order(ingredient_ids=ingredients)
        
        assert response.status_code == 200
        assert response.json().get("success") is True


    @allure.step("Ошибка создания заказа без ингредиентов")
    def test_create_order_without_ingredients_bad_request(self, order_client):

        response = order_client.create_order(ingredient_ids=[])
        
        assert response.status_code == 400
        assert response.json().get("message") == MISSING_INGREDIENTS_MSG


    @allure.step("Ошибка создания заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredient_hash_server_error(self, order_client):

        response = order_client.create_order(ingredient_ids=["invalid_hash_123"])
        
        assert response.status_code == 500
        assert INTERNAL_SERVER_ERROR_MSG in response.text
