import reflex as rx
from ..models import Product

class DeleteState(rx.State):
    form_data: dict = {}
    
    @rx.event
    def delete_product(self, form_data: dict):
        with rx.session() as session:
            product = session.exec(
                Product.select().where(
                    Product.name == form_data['product_name']
                )
            ).first()
            session.delete(product)
            session.commit()

            return rx.redirect('/show_products')
        