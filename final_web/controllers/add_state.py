import reflex as rx
from ..models import Product

class AddState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data # Takes all the data from the form (it is a page)

        with rx.session() as session:
            session.add(
                Product(
                    name=form_data['product_name'],
                    price=form_data['product_price'],
                )
            )
            session.commit()

        return rx.redirect('/show_product') 

