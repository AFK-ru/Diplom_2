import random
import string

def generate_random_string(length=10):

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_user_data():

    username = generate_random_string(8)
    return {
        "email": f"{username}@yandex.ru",
        "password": generate_random_string(10),
        "name": username
    }
