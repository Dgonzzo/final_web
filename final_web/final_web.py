import reflex as rx
from rxconfig import config

# Imports from components
from .components import sidebar_bottom_profile

# Imports from pages
from .pages import main_page

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        sidebar_bottom_profile(),
        main_page()
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
