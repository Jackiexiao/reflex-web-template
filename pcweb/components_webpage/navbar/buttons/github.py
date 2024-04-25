import reflex as rx

from .style import button_style


def shorten_to_k(number):
    if number >= 1000:
        return f"{number / 1000:.0f}k+"
    else:
        return str(number)


def github_desktop() -> rx.Component:
    return rx.link(
        rx.flex(
            rx.icon(
                "github",
                color=rx.color("mauve", 9),
            ),
            rx.text(
                "Github",
                color=rx.color("mauve", 9),
            ),
            rx.text(
                "15k",
                background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                border_radius="5px",
                padding="0px 3px",
                color=rx.color("mauve", 9),
            ),
            spacing="2",
            style=button_style,
        ),
        href="https://github.com/reflex-dev/reflex",
    )


def github_mobile() -> rx.Component:
    return rx.link(
        rx.flex(
            rx.icon(
                "github",
                color="#6f6d78",
            ),
            padding="7px",
            style=button_style,
            border_radius="8px",
        ),
        href="https://github.com/reflex-dev/reflex",
    )


def github() -> rx.Component:
    return rx.fragment(
        rx.desktop_only(github_desktop()), rx.mobile_and_tablet(github_mobile())
    )
