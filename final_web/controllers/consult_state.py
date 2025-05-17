import reflex as rx
from ..models import Product

class ConsultState(rx.State):
    form_data: dict = {}
    actual_product: Product = None

    @rx.var
    def get_name_my(self) -> str:
        return self.router.page.params.get('name')
    
    @rx.event
    def update_price(self, value):
        self.actual_product.price = float(value)

    @rx.event
    def update_name(self,value):
        self.actual_product.name = str(value)

    @rx.event
    def get_product(self):
        with rx.session() as session:
            self.actual_product = session.exec(
                Product.select().where(
                    Product.name == self.get_name_my
                )
            ).one_or_none()
    

    @rx.event
    def handle_submit_update(self):
        with rx.session() as session:
            product = session.exec(
                Product.select().where(
                    Product.name == self.get_name_my
                )
            ).one_or_none()

            # Add more as the parameters increase
            product.name = self.actual_product.name
            product.price = self.actual_product.price
            
            session.add(product)
            session.commit()

        return rx.redirect('/show_products') 
    
    @rx.event
    def handle_submit_delete(self):
        with rx.session() as session:
            product = session.exec(
                Product.name == self.get_name_my
            ).first()
            session.delete(product)
            session.commit()
        
        return rx.redirect('/show_products')
