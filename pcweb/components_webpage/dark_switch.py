import reflex as rx
from reflex.style import toggle_color_mode

button_style = {
    "border_radius": "50px",
    "border": f"1px solid {rx.color('mauve', 4)}",
    "background": rx.color("mauve", 2),
    "box_shadow": "0px 3px 7px -4px rgba(21, 18, 44, 0.15)",
    "padding": "7px 12px 7px 12px",
    "align_items": "center",
}


def dark_switch() -> rx.Component:
    return rx.flex(
        rx.color_mode.icon(
            light_component=rx.icon("sun", color=rx.color("mauve", 9)),
            dark_component=rx.icon("moon", color=rx.color("mauve", 9)),
        ),
        on_click=toggle_color_mode,
        _hover={"cursor": "pointer"},
        padding="7px",
        style=button_style,
        border_radius="8px",
    )
