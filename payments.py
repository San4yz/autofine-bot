import stripe
from config import STRIPE_API_KEY, PRICE_ID

stripe.api_key = STRIPE_API_KEY

def create_payment_link():
    session = stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{"price": PRICE_ID, "quantity": 1}],
        success_url="https://t.me/AutoFine_EU_Bot",
        cancel_url="https://t.me/AutoFine_EU_Bot",
    )
    return session.url
