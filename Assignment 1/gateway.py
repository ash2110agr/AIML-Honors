from abc import ABC, abstractmethod
from modes import create_mode


class Gateway(ABC):

    def __init__(self, name, fee_pct):
        self.name = name
        self.fee_pct = fee_pct

    @abstractmethod
    def gateway_key(self):
        pass

    def process(self, method, amount, **kwargs):
        mode = create_mode(self.gateway_key(), method, **kwargs)
        print(f"\n[{self.name}] {mode.info()}")

        fee = round(amount * self.fee_pct, 2)
        total = amount + fee
        print(f"Subtotal: Rs {amount:.2f}")
        print(f"Fee ({self.fee_pct*100:.1f}%): Rs {fee:.2f}")
        print(f"Total: Rs {total:.2f}")

        return mode.execute(total)


class RazorpayGateway(Gateway):

    def __init__(self):
        super().__init__("Razorpay", 0.02)

    def gateway_key(self):
        return "razorpay"


class StripeGateway(Gateway):

    def __init__(self):
        super().__init__("Stripe", 0.029)

    def gateway_key(self):
        return "stripe"


GATEWAYS = {
    "razorpay": RazorpayGateway,
    "stripe": StripeGateway,
}


def get_gateway(name):
    name = name.lower()
    if name not in GATEWAYS:
        raise ValueError(f"Unknown gateway: {name}")
    return GATEWAYS[name]()
