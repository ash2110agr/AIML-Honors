from gateway import get_gateway


def run():
    gw_name = input("Pick gateway (stripe/razorpay): ").strip().lower()
    gw = get_gateway(gw_name)

    method = input("Payment method (card/upi): ").strip().lower()

    if method == "card":
        card_num = input("Card number: ").strip()
        details = {"card_number": card_num}
    elif method == "upi":
        upi = input("UPI ID: ").strip()
        details = {"upi_id": upi}
    else:
        print("Not a valid method.")
        return

    amt = float(input("Amount in Rs: "))
    if amt <= 0:
        print("Amount should be positive.")
        return

    result = gw.process(method, amt, **details)
    if result:
        print("\nDone, payment went through.")


if __name__ == "__main__":
    run()
