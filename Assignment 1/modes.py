from abc import ABC, abstractmethod


class PaymentMode(ABC):

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def execute(self, amount):
        pass


class RazorpayCard(PaymentMode):

    def __init__(self, card_number):
        self._card = card_number

    def info(self):
        return f"Razorpay Card ending {self._card[-4:]}"

    def execute(self, amount):
        print(f"Charged Rs {amount:.2f} via Razorpay Card")
        return True


class RazorpayUPI(PaymentMode):

    def __init__(self, upi_id):
        self._upi = upi_id

    def info(self):
        return f"Razorpay UPI: {self._upi}"

    def execute(self, amount):
        print(f"Charged Rs {amount:.2f} via Razorpay UPI")
        return True


class StripeCard(PaymentMode):

    def __init__(self, card_number):
        self._card = card_number

    def info(self):
        return f"Stripe Card ending {self._card[-4:]}"

    def execute(self, amount):
        print(f"Charged Rs {amount:.2f} via Stripe Card")
        return True


class StripeUPI(PaymentMode):

    def __init__(self, upi_id):
        self._upi = upi_id

    def info(self):
        return f"Stripe UPI: {self._upi}"

    def execute(self, amount):
        print(f"Charged Rs {amount:.2f} via Stripe UPI")
        return True


# maps (gateway, method) -> class
MODE_REGISTRY = {
    ("razorpay", "card"): RazorpayCard,
    ("razorpay", "upi"):  RazorpayUPI,
    ("stripe", "card"):   StripeCard,
    ("stripe", "upi"):    StripeUPI,
}


def create_mode(gateway, method, **kwargs):
    key = (gateway.lower(), method.lower())
    if key not in MODE_REGISTRY:
        raise ValueError(f"No mode for {gateway}/{method}")
    return MODE_REGISTRY[key](**kwargs)
