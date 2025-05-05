import reflex as rx

class Product(rx.Model, table=True):
    name: str
    price: float
