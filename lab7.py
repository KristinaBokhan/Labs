from abc import ABC, abstractmethod

# Базовий клас для стратегій доставки
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_delivery_cost(self, distance: float) -> float:
        """
        Метод для обчислення вартості доставки
        :param distance: Відстань до місця доставки
        :return: Вартість доставки
        """
        pass

# Стратегія "Самовивіз"
class PickupStrategy(DeliveryStrategy):
    def calculate_delivery_cost(self, distance: float) -> float:
        """
        Самовивіз завжди безкоштовний
        """
        return 0.0

# Стратегія "Доставка зовнішньою службою доставки"
class ExternalDeliveryServiceStrategy(DeliveryStrategy):
    def calculate_delivery_cost(self, distance: float) -> float:
        """
        Вартість доставки зовнішньою службою залежить від відстані
        :param distance: Відстань до місця доставки
        :return: Вартість доставки
        """
        return distance * 1.5  # Наприклад, 1.5 одиниці за км

# Стратегія "Доставка власною службою доставки"
class OwnDeliveryServiceStrategy(DeliveryStrategy):
    def calculate_delivery_cost(self, distance: float) -> float:
        """
        Вартість доставки власною службою фіксована до певної відстані
        :param distance: Відстань до місця доставки
        :return: Вартість доставки
        """
        if distance <= 5:
            return 5.0  # Фіксована вартість для відстаней <= 5 км
        else:
            return 5.0 + (distance - 5) * 2  # Додаткова плата за кожен км понад 5 км

# Контекст, що використовує стратегії доставки
class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        """
        Ініціалізація контексту зі стратегією
        :param strategy: Стратегія доставки
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy):
        """
        Встановити нову стратегію
        :param strategy: Нова стратегія доставки
        """
        self._strategy = strategy

    def calculate_cost(self, distance: float) -> float:
        """
        Виклик стратегії для обчислення вартості
        :param distance: Відстань до місця доставки
        :return: Вартість доставки
        """
        return self._strategy.calculate_delivery_cost(distance)

# Приклад використання
if __name__ == "__main__":
    # Нехай відстань до місця доставки 10 км
    distance = 10.0

    pickup = PickupStrategy()
    context = DeliveryContext(pickup)
    print(f"Самовивіз: {context.calculate_cost(distance)} одиниць")

    external_delivery = ExternalDeliveryServiceStrategy()
    context.set_strategy(external_delivery)
    print(f"Доставка зовнішньою службою: {context.calculate_cost(distance)} одиниць")

    own_delivery = OwnDeliveryServiceStrategy()
    context.set_strategy(own_delivery)
    print(f"Доставка власною службою: {context.calculate_cost(distance)} одиниць")
