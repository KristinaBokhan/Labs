from datetime import date
from typing import List

class FormComponent:
    def __init__(self, mediator=None):
        self.mediator = mediator

    def set_mediator(self, mediator):
        self.mediator = mediator

    def notify(self, event):
        if self.mediator:
            self.mediator.notify(self, event)

class DeliveryDateSelector(FormComponent):
    def __init__(self):
        super().__init__()
        self.selected_date = None

    def select_date(self, delivery_date: date):
        self.selected_date = delivery_date
        self.notify("date_selected")

class TimeSlotSelector(FormComponent):
    def __init__(self):
        super().__init__()
        self.slots = []

    def update_slots(self, slots: List[str]):
        self.slots = slots

class RecipientCheckbox(FormComponent):
    def __init__(self):
        super().__init__()
        self.other_recipient = False

    def set_other_recipient(self, value: bool):
        self.other_recipient = value
        self.notify("other_recipient_changed")

class RecipientDetails(FormComponent):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.phone = ""

class SelfPickupCheckbox(FormComponent):
    def __init__(self):
        super().__init__()
        self.self_pickup = False

    def set_self_pickup(self, value: bool):
        self.self_pickup = value
        self.notify("self_pickup_changed")

class OrderMediator:
    def __init__(self):
        self.delivery_date_selector = None
        self.time_slot_selector = None
        self.recipient_checkbox = None
        self.recipient_details = None
        self.self_pickup_checkbox = None

    def link_components(self, delivery_date_selector, time_slot_selector, recipient_checkbox, recipient_details, self_pickup_checkbox):
        self.delivery_date_selector = delivery_date_selector
        self.time_slot_selector = time_slot_selector
        self.recipient_checkbox = recipient_checkbox
        self.recipient_details = recipient_details
        self.self_pickup_checkbox = self_pickup_checkbox

        # Установлення посередника для кожного компонента
        self.delivery_date_selector.set_mediator(self)
        self.time_slot_selector.set_mediator(self)
        self.recipient_checkbox.set_mediator(self)
        self.recipient_details.set_mediator(self)
        self.self_pickup_checkbox.set_mediator(self)

    def notify(self, sender: FormComponent, event: str):
        if event == "date_selected" and sender == self.delivery_date_selector:
            self.refresh_time_slots()
        elif event == "other_recipient_changed" and sender == self.recipient_checkbox:
            self.toggle_recipient_fields(self.recipient_checkbox.other_recipient)
        elif event == "self_pickup_changed" and sender == self.self_pickup_checkbox:
            self.toggle_delivery_fields(self.self_pickup_checkbox.self_pickup)

    def refresh_time_slots(self):
        if self.delivery_date_selector.selected_date:
            self.time_slot_selector.update_slots(["9-11", "12-14", "15-17"])

    def toggle_recipient_fields(self, other_recipient: bool):
        if other_recipient:
            print("Поля для іншого отримувача тепер обов'язкові.")
        else:
            print("Поля для іншого отримувача не обов'язкові.")

    def toggle_delivery_fields(self, self_pickup: bool):
        if self_pickup:
            print("Всі поля, пов'язані з доставкою, вимкнено.")
        else:
            print("Поля доставки увімкнено.")
