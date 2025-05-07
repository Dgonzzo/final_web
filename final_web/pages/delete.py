import reflex as rx
from ..controllers import DeleteState

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
                rx.button("Submit", type="submit"),
            ),
            on_submit = DeleteState.delete_product,
            reset_on_submit=True,
        ),
        align="center",
        justify="center",
    )

def delete_product_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.text("Delete a product", size="9"),
            form_add_product(),  
        )
    ),