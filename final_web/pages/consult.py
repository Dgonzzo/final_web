import reflex as rx

from ..controllers import ConsultState

def form_consult():
    return rx.vstack(
            rx.form(
                rx.vstack(
                    rx.input(
                        value= ConsultState.actual_product.name,
                        placeholder="Name (put the old name to keep it)",
                        name="product_name",
                        on_change = ConsultState.update_name,
                    ),
                    rx.input(
                        value= ConsultState.actual_product.price,
                        placeholder="Price",
                        name="product_price",
                        on_change = ConsultState.update_price
                    ),
                    rx.hstack(
                        rx.button("Modify", type="button", color_scheme="green", on_click=ConsultState.handle_submit_update),
                        # rx.button("Delete", type="button", color_scheme="red", on_click=ConsultState.handle_submit_delete)
                    )
                    
                ),
                reset_on_submit=True,
            ),
    )

def consult_product_page():
    return rx.container(
            rx.vstack(
                rx.heading("Modify"),
                form_consult(),
            )            
        ),
