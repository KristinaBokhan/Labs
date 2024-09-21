from abc import ABC, abstractmethod


# Базовий клас для соціальних мереж
class SocialNetwork(ABC):
    @abstractmethod
    def login(self, username: str, password: str):
        pass

    @abstractmethod
    def publish(self, message: str):
        pass


# Facebook клас, що реалізує базовий клас SocialNetwork
class Facebook(SocialNetwork):
    def login(self, login: str, password: str):
        print(f"Logging into Facebook with login: {login}")

    def publish(self, message: str):
        print(f"Publishing message on Facebook: {message}")


# LinkedIn клас, що реалізує базовий клас SocialNetwork
class LinkedIn(SocialNetwork):
    def login(self, email: str, password: str):
        print(f"Logging into LinkedIn with email: {email}")

    def publish(self, message: str):
        print(f"Publishing message on LinkedIn: {message}")


# Фабричний метод для створення соціальних мереж
class SocialNetworkFactory(ABC):
    @abstractmethod
    def create_social_network(self) -> SocialNetwork:
        pass


# Фабрика для Facebook
class FacebookFactory(SocialNetworkFactory):
    def create_social_network(self) -> SocialNetwork:
        return Facebook()


# Фабрика для LinkedIn
class LinkedInFactory(SocialNetworkFactory):
    def create_social_network(self) -> SocialNetwork:
        return LinkedIn()


# Клієнтський код для публікації повідомлення в соціальних мережах
def publish_message(factory: SocialNetworkFactory, credentials: dict, message: str):
    # Створюємо соціальну мережу через фабрику
    social_network = factory.create_social_network()

    # Логін в соцмережу
    social_network.login(**credentials)

    # Публікація повідомлення
    social_network.publish(message)


if __name__ == "__main__":
    # Приклад публікації повідомлення в Facebook
    facebook_factory = FacebookFactory()
    facebook_credentials = {"login": "user_facebook", "password": "facebook_pass"}
    publish_message(facebook_factory, facebook_credentials, "Hello, Facebook!")

    # Приклад публікації повідомлення в LinkedIn
    linkedin_factory = LinkedInFactory()
    linkedin_credentials = {"email": "user_linkedin@example.com", "password": "linkedin_pass"}
    publish_message(linkedin_factory, linkedin_credentials, "Hello, LinkedIn!")
