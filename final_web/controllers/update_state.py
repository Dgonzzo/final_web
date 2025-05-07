import reflex as rx
from ..models import Product

class UpdateState(rx.State):
    form_data: dict = {}

    def modify_product(self, form_data: dict):
        with rx.session() as session:
            product = session.exec(
                Product.select().where(
                    (Product.name == form_data['product_name'])
                )
            ).first()
            product.name = form_data['new_product_name'] 
            # User will have to insert again the old name in order to only change the price
            product.price = form_data['new_product_price']
            
            session.add(product)
            session.commit()

        return rx.redirect('/show_products')