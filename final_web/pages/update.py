import reflex as rx
from ..controllers import UpdateState

'''
Field name on each rx.input is used to identify the input field in the form submission.
! Important: check that the name used is the same as the one used in the controller.
'''

def form_add_product():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Name",
                    name="product_name",
                ),
                rx.input(
                    placeholder="New Name (insert the old name to keep it)",
                    name="new_product_name",
                ),
                rx.input(
                    placeholder="New Price",
                    name="new_product_price",
                ),

                rx.button("Submit", type="submit"),
            ),
            on_submit=UpdateState.modify_product,
            reset_on_submit=True,
        ),
        align="center",
        justify="center",
    )

def add_product_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text("Update a product", size="9"),
            form_add_product(),  
        )
    ),