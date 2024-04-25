import reflex as rx

from pcweb import constants, styles
from pcweb.components_webpage.logo import logo
from pcweb.templates.webpage import webpage


def change(date, title, description, points, link):
    return rx.vstack(
        rx.vstack(
            logo(
                width=["10em", "12em", "14em"],
            ),
            rx.hstack(
                rx.hstack(
                    rx.icon(tag="copy", size=18, color="#6C6C81"),
                    rx.text(title, font_weight=styles.BOLD_WEIGHT),
                ),
                rx.tablet_and_desktop(
                    rx.divider(margin_x="1em", size="4"),
                    width="100%",
                ),
                rx.link(
                    rx.button(
                        rx.icon(tag="github", size=18),
                        "Full Notes ->",
                        color="#A2A2B9",
                        padding_x="1em",
                        border_radius="7px;",
                        border="1px solid rgba(107, 107, 127, 0.50);",
                        background="rgba(107, 107, 127, 0.10);",
                        box_shadow="0px 3px 4px -1px rgba(23, 26, 43, 0.40);",
                        backdrop_filter="blur(2px);",
                        text_wrap="nowrap",
                    ),
                    href=link,
                ),
                width="100%",
                padding_top=["1em", "1em", "0", "0", "0", "0"],
                justify="between",
            ),
            padding_right="1em",
            border_radius="10px",
            border="1px solid #3C3646",
            # background="linear-gradient(115deg, #1D1B23 14.13%, #131217 73.41%)",
            # box_shadow="0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset, 0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
            padding="1em",
            padding_top="2em",
            width="100%",
        ),
        rx.text(description, font_family=styles.MONO),
        rx.chakra.unordered_list(
            *[
                rx.list_item(
                    d, font_size=".8em", color="#6C6C81", font_family=styles.MONO
                )
                for d in points
            ],
            padding_left="1.5em",
        ),
        align_items="flex-start",
        width="100%",
        padding_bottom="3em",
        padding_left=["0", "0", "1em", "1em", "1em", "1em"],
        border_left="1px solid #23222B",
    )


def changelog_content():
    return rx.chakra.vstack(
        change(
            "2024-04-22",
            "v0.4.9",
            "Bug Fixes and Various Improvements",
            [
                "Fix for UnicodeDecodeError on Windows",
                "Use npm fallback when bun does not work",
                "Allow set in Var.contains",
                "Fix for light/dark dialogs not matching current theme appearance",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.9",
        ),
        change(
            "2024-04-15",
            "v0.4.8",
            "Support Bun on Windows for Faster Dependency Installation",
            [
                "Expose transpile_packages for Components that do not identify as ES6 module",
                "Enum types are serialized to their values",
                "Automatic tuple unpacking for Component children",
            ],
            "https://github.com/reflex-dev/reflex/releases/tag/v0.4.8",
        ),
        width="100%",
    )


@webpage(path="/changelog", title="Changelog · Reflex")
def changelog():
    return rx.center(
        rx.box(
            rx.flex(
                rx.chakra.text(
                    "Timeline",
                    # background_image="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                    text_align="center",
                    # background_clip="text",
                    padding_x="1em",
                ),
                width="7em",
                justify="center",
                border_radius="15px;",
                border="1px solid #4435D4;",
                # background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
                # box_shadow="0px 3px 6px -3px rgba(34, 25, 121, 0.60), 0px 0px 4px -1px rgba(27, 21, 90, 0.40);",
            ),
            rx.chakra.text(
                "Changelog",
                font_size="44px",
                # background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                # background_clip="text",
                font_weight="bold",
                letter_spacing="-1.28px;",
            ),
            rx.center(
                rx.chakra.span(
                    "Reflex has new releases and features coming every week! Make sure to star and watch on ",
                    rx.link("GitHub", href=constants.GITHUB_URL, color="#6151F3"),
                    " to stay up to date.",
                    # color="#A2A2B9",
                    width="100%",
                ),
                font_family=styles.MONO,
                padding="1em",
                margin_bottom="2em",
                border_radius="7px;",
                border="1px solid rgba(107, 107, 127, 0.50);",
                # background="rgba(107, 107, 127, 0.10);",
                # box_shadow="0px 3px 4px -1px rgba(23, 26, 43, 0.40);",
                backdrop_filter="blur(2px);",
                width="100%",
            ),
            changelog_content(),
            max_width=["95vw", "95vw", "100vw", "100vw", "100vw", "100vw"],
        ),
        width="100%",
    )
