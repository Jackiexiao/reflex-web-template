"""UI and logic for the navbar component."""

import reflex as rx

from pcweb import constants
from pcweb.components_webpage.dark_switch import dark_switch
from pcweb.pages.changelog import changelog
from pcweb.pages.faq import faq

from .buttons.discord import discord
from .buttons.github import github
from .buttons.sidebar import sidebar_button


class NavbarState(rx.State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_input: str = ""

    enter: bool = False

    banner: bool = True

    ai_chat: bool = True

    current_category = "All"

    def toggle_banner(self):
        self.banner = not self.banner

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    def toggle_ai_chat(self):
        self.ai_chat = not self.ai_chat

    def update_category(self, tag):
        self.current_category = tag


def banner():
    return rx.cond(
        NavbarState.banner,
        rx.box(
            rx.hstack(
                rx.text(
                    " 🚀 Reflex live on Product Hunt! Check out our launch ",
                    rx.link(
                        "here",
                        href="https://www.producthunt.com/posts/reflex-6",
                        style={
                            "text_decoration": "underline",
                        },
                        color="#fff",
                        is_external=True,
                    ),
                    ". 🎉",
                    font_weight=600,
                    text_align="center",
                    width="100%",
                ),
                rx.icon(
                    tag="x",
                    z_index=1000,
                    on_click=NavbarState.toggle_banner,
                ),
                width="100%",
                align_items="center",
            ),
            color="#fff",
            background_color=rx.color("violet", 9),
            border_bottom=f"1px solid {rx.color('mauve', 4)}",
            padding_y=["0.8em", "0.8em", "0.5em"],
            width="100%",
        ),
    )


def resource_header(text):
    return rx.text(
        text,
        color="#fff",
        padding_bottom="10px",
        font_weight="600",
    )


def resources_item(text, url, icon):
    return rx.link(
        rx.flex(
            rx.icon(icon, size=20, color=rx.color("mauve", 9)),
            rx.text(text, color=rx.color("mauve", 9)),
            wrap="nowrap",
            spacing="2",
        ),
        href=url,
    )


def resources_section(style):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.flex(
                rx.text("Resources", style=style),
                rx.icon(tag="chevron_down", size=18, style=style),
                align_items="center",
                _hover={
                    "cursor": "pointer",
                },
                spacing="2",
            )
        ),
        rx.hover_card.content(
            rx.flex(
                rx.flex(
                    resource_header("Open Source"),
                    resources_item("Github", "https://github.com/reflex-dev", "github"),
                    resources_item(
                        "Github Discussions",
                        "https://github.com/orgs/reflex-dev/discussions",
                        "message-circle-question",
                    ),
                    resources_item(
                        "Contribute to Reflex",
                        constants.CONTRIBUTING_URL,
                        "file-json-2",
                    ),
                    resources_item("Changelog", changelog.path, "list-checks"),
                    direction="column",
                    align_items="start",
                    padding_left="20px",
                    padding_y="20px",
                    spacing="2",
                ),
                rx.flex(
                    resource_header("Resources"),
                    resources_item(
                        "Roadmap",
                        constants.ROADMAP_URL,
                        "map-pinned",
                    ),
                    resources_item("FAQ", faq.path, "list-todo"),
                    direction="column",
                    align_items="start",
                    padding_top="20px",
                    padding_bottom="20px",
                    spacing="2",
                ),
                rx.flex(
                    direction="column",
                    background="linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
                    border_left="1px solid rgba(29, 29, 32, 0.08);",
                    align_items="start",
                    height="210px",
                    padding_top="20px",
                    padding_left="20px",
                    padding_bottom="20px",
                    padding_right="20px",
                    spacing="2",
                ),
                spacing="6",
            ),
            border="1px solid rgba(29, 29, 32, 0.08);",
            background="linear-gradient(180deg, rgba(29, 27, 33, 0.95) 0%, rgba(20, 19, 24, 0.95) 100%);",
            box_shadow="0px 24px 54px -17px rgba(13, 12, 16, 0.30), 0px 0px 0px 1px rgba(93, 93, 107, 0.29), 0px 0px 64px 5px rgba(53, 51, 60, 0.30) inset;",
            max_width="1000px",
            height="210px",
            padding="0",
            overflow="hidden",
        ),
    )


def navigation_section():
    section_style = {
        "color": "#6C6C81",
        "font-weight": "400",
    }

    return rx.box(
        rx.flex(
            rx.link("FAQ", href=faq.path, style=section_style),
            rx.link("ChangeLog", href=changelog.path, style=section_style),
            resources_section(style=section_style),
            spacing="5",
        ),
        display=["none", "none", "none", "none", "flex", "flex"],
    )


def blur_background():
    return rx.fragment(
        rx.script(
            """
            window.onscroll = function() {
                var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                var scrollThreshold = 100;
                var navbar = document.getElementById('navbar');
                if (!navbar) {
                    return;
                }

                if (scrollTop > scrollThreshold) {
                    navbar.classList.add('blur-navbar');
                } else {
                    navbar.classList.remove('blur-navbar');
                }
            };
            """
        ),
        rx.html(
            """
            <style>
            .blur-navbar {
                border: 1px solid rgba(29, 29, 32, 0.08);
                background: linear-gradient(180deg, rgba(29, 27, 33, 0.98) 0%, rgba(20, 19, 24, 0.98) 100%);
                box-shadow: 0px 24px 54px -17px rgba(13, 12, 16, 0.30), 0px 0px 0px 1px rgba(93, 93, 107, 0.29), 0px 0px 64px 5px rgba(53, 51, 60, 0.30) inset;
                backdrop-filter: blur(20px);
            }
            </style>
            """
        ),
    )


def navbar(sidebar: rx.Component = None) -> rx.Component:
    return rx.flex(
        banner(),
        rx.flex(
            rx.link(
                rx.box(
                    rx.color_mode_cond(
                        rx.image(
                            src="/logos/light/reflex.svg",
                            alt="Reflex Logo",
                            height="20px",
                            justify="start",
                        ),
                        rx.image(
                            src="/logos/dark/reflex.svg",
                            alt="Reflex Logo",
                            height="20px",
                            justify="start",
                        ),
                    ),
                ),
                href="/",
            ),
            navigation_section(),
            rx.box(
                flex_grow="1",
            ),
            blur_background(),
            rx.flex(
                github(),
                rx.box(
                    discord(),
                    display=["none", "none", "none", "none", "flex", "flex"],
                ),
                rx.box(
                    dark_switch(),  # or `color()` in reflex-web repo
                    # display=["none", "none", "none", "none", "flex", "flex"],
                ),
                rx.box(
                    sidebar_button(sidebar),
                    display=["flex", "flex", "flex", "flex", "none", "none"],
                ),
                spacing="3",
                align_items="center",
            ),
            background_color=rx.color("mauve", 1),
            border_bottom=f"1px solid {rx.color('mauve', 4)}",
            width="100%",
            align_items="center",
            spacing="5",
            padding="7px 20px 7px 20px;",
        ),
        width="100%",
        z_index="5",
        top="0px",
        position="fixed",
        align_items="center",
        direction="column",
    )
