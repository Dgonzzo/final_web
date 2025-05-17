import reflex as rx
from rxconfig import config

# Imports from components
from .components import sidebar_bottom_profile

# Imports from controllers
from .controllers import ListState
from .controllers import ConsultState

# Imports from pages
from .pages import main_page
from .pages import show_list
from .pages import add_product_page
#! from .pages import update_product_page 
from .pages import delete_product_page
from .pages import consult_product_page

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        sidebar_bottom_profile(),
        main_page()
    )

def show_products() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        rx.vstack(
            show_list(),
            justify="center",
            min_height="85vh",
        )
    )

def add_product() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        rx.vstack(
            add_product_page(),
            justify="center",
            min_height="85vh",
        )
    )

def delete_product() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        rx.vstack(
            # update_product_page(),
            delete_product_page(),
            justify="center",
            min_height="85vh",
        )
    )

def consult_product() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        consult_product_page(),
    )


app = rx.App(
    theme = rx.theme(
        appearance = "inherit",
        has_background = True,
        radius = 'large',
        accent_color = "brown",
        gray_color = "sand",
    ),
)
app.add_page(index)
app.add_page(show_products, route='show_products', on_load = ListState.get_products)
app.add_page(add_product, route='add_product')
app.add_page(delete_product, route='update_delete_product')
app.add_page(consult_product_page, route='consult/[name]', on_load=ConsultState.get_product)
