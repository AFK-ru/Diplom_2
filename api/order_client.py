import allure
from api.base_client import BaseClient
from data.urls import ORDERS, INGREDIENTS

class OrderClient(BaseClient):

    @allure.step("Получение актуального списка ингредиентов с сервера")
    def get_ingredients(self):

        return self.get(INGREDIENTS)


    @allure.step("Оформление заказа. Ингредиенты: {ingredient_ids}")
    def create_order(self, ingredient_ids, token=None):

        payload = {"ingredients": ingredient_ids}
        headers = {"Authorization": token} if token else None

        return self.post(ORDERS, payload=payload, headers=headers)
