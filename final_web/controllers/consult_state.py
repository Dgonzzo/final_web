import reflex as rx
from ..models import Product

class ConsultState(rx.State):
    form_data: dict = {}
    actual_product: Product = None

    @rx.var
    def get_name(self):
        return self.router.page.params.get('name')

    @rx.var
    def get_product(self):
        with rx.session() as session:
            self.actual_product = session.exec(
                Product.select().where(
                    Product.name == self.get_name
                )
            ).one_or_none()
