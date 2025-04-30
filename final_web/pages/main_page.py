import reflex as rx

def main_page() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to your inventory!", size="9"),
            # rx.link(
            #     rx.button("Check out our docs!"),
            #     href="https://reflex.dev/docs/getting-started/introduction/",
            #     is_external=True,
            # ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )