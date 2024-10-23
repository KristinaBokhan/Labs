from abc import ABC, abstractmethod

class BaseEntity(ABC):
    def update_entity(self, data):
        entity = self.get_entity(data)

        if not self.validate_data(entity):
            self.on_validation_failed(entity)
            return self.generate_response(400, "Validation Failed")

        self.save_entity(entity)

        return self.generate_response(200, "Update Successful", entity)

    @abstractmethod
    def get_entity(self, data):
        """Отримати сутність для оновлення"""
        pass

    @abstractmethod
    def validate_data(self, entity):
        """Перевірити валідність даних"""
        pass

    @abstractmethod
    def save_entity(self, entity):
        """Зберегти сутність"""
        pass

    def on_validation_failed(self, entity):
        """Хук для дій, якщо валідація не пройшла (можна перевизначити)"""
        pass

    def generate_response(self, code, status, entity=None):
        """Генерація відповіді"""
        return {
            "code": code,
            "status": status,
            "data": entity if entity else {}
        }

class Product(BaseEntity):
    def get_entity(self, data):
        return data

    def validate_data(self, entity):
        return "name" in entity and entity["price"] > 0

    def save_entity(self, entity):
        print(f"Saving product: {entity}")

    def on_validation_failed(self, entity):
        print(f"Validation failed for product: {entity}. Sending notification to admin.")

class User(BaseEntity):
    def get_entity(self, data):
        return data

    def validate_data(self, entity):
        return "name" in entity and (not "email" in entity or entity["email"] == entity.get("old_email"))

    def save_entity(self, entity):
        print(f"Saving user: {entity}")

class Order(BaseEntity):
    def get_entity(self, data):
        return data

    def validate_data(self, entity):
        return "order_id" in entity and len(entity["items"]) > 0

    def save_entity(self, entity):
        print(f"Saving order: {entity}")

    def generate_response(self, code, status, entity=None):
        return {
            "code": code,
            "status": status,
            "order": entity if entity else {}
        }

if __name__ == "__main__":
    product_data = {"name": "Laptop", "price": 1200}
    product = Product()
    response = product.update_entity(product_data)
    print(response)

    user_data = {"name": "John Doe", "old_email": "john@example.com", "email": "john@example.com"}
    user = User()
    response = user.update_entity(user_data)
    print(response)

    order_data = {"order_id": 123, "items": ["item1", "item2"]}
    order = Order()
    response = order.update_entity(order_data)
    print(response)
