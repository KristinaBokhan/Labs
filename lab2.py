from abc import ABC, abstractmethod


class SocialNetwork(ABC):
    @abstractmethod
    def login(self, username: str, password: str):
        pass

    @abstractmethod
    def publish(self, message: str):
        pass


class Facebook(SocialNetwork):
    def login(self, login: str, password: str):
        print(f"Logging into Facebook with login: {login}")

    def publish(self, message: str):
        print(f"Publishing message on Facebook: {message}")


class LinkedIn(SocialNetwork):
    def login(self, email: str, password: str):
        print(f"Logging into LinkedIn with email: {email}")

    def publish(self, message: str):
        print(f"Publishing message on LinkedIn: {message}")



class SocialNetworkFactory(ABC):
    @abstractmethod
    def create_social_network(self) -> SocialNetwork:
        pass



class FacebookFactory(SocialNetworkFactory):
    def create_social_network(self) -> SocialNetwork:
        return Facebook()



class LinkedInFactory(SocialNetworkFactory):
    def create_social_network(self) -> SocialNetwork:
        return LinkedIn()



def publish_message(factory: SocialNetworkFactory, credentials: dict, message: str):
    
    social_network = factory.create_social_network()

    social_network.login(**credentials)

    social_network.publish(message)


if __name__ == "__main__":

    facebook_factory = FacebookFactory()
    facebook_credentials = {"login": "user_facebook", "password": "facebook_pass"}
    publish_message(facebook_factory, facebook_credentials, "Hello, Facebook!")

   
    linkedin_factory = LinkedInFactory()
    linkedin_credentials = {"email": "user_linkedin@example.com", "password": "linkedin_pass"}
    publish_message(linkedin_factory, linkedin_credentials, "Hello, LinkedIn!")
