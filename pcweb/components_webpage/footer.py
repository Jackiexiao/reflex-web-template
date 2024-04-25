import json
import os
from datetime import datetime

import httpx
import reflex as rx
from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field

from pcweb import constants, styles
from pcweb.components_webpage.logo import logo
from pcweb.pages.index import index

footer_item_style = {
    "font_family": styles.SANS,
    "font_weight": "500",
    "_hover": {"color": rx.color("accent", 5)},
    "color": "#6C6C81",
}

footer_style = {
    "box_shadow": "medium-lg",
    "border_top": f"0.1em solid {rx.color('accent', 5)}",
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
    "padding_x": styles.PADDING_X2,
    "bg": "#110F1F",
}


def prompt_sign():
    return rx.chakra.text(
        "$",
        color=rx.color("accent"),
        font_family=styles.SANS,
        style={"userSelect": "none"},
    )


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )


number_color = "#4E5A6A"
text_color = "#A9ABD8"
other_color = "#5646ED"
bottom_color = "#6C6C81"


class Waitlist(rx.Model, table=True):
    email: str
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class IndexState(rx.State):
    """Hold the state for the home page."""

    # The waitlist email.
    email: str

    # Whether the user signed up for the waitlist.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def add_contact_to_loops(self, contact_data):
        url = "https://app.loops.so/api/v1/contacts/create"
        loops_api_key = os.getenv("LOOPS_API_KEY")
        if loops_api_key is None:
            print("Loops API key does not exist")
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {loops_api_key}",
        }

        try:
            with httpx.Client() as client:
                response = client.post(url, headers=headers, json=contact_data)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        except httpx.RequestError as e:
            print(f"An error occurred: {e}")

    def signup(self):
        """Sign the user up for the waitlist."""
        # Check if the email is valid.
        try:
            validation = validate_email(self.email, check_deliverability=True)
            self.email = validation.email
        except EmailNotValidError as e:
            # Alert the error message.
            return rx.window_alert(str(e))

        # Check if the user is already on the waitlist.
        with rx.session() as session:
            user = session.query(Waitlist).filter(Waitlist.email == self.email).first()
            if user is None:
                # Add the user to the waitlist.
                session.add(Waitlist(email=self.email))
                session.commit()
                contact_data = json.dumps({"email": self.email})
                self.add_contact_to_loops(contact_data)

        self.signed_up = True


button_style = {
    "border_radius": "50px",
    "": "",
    "padding": "7px 12px 7px 12px",
    "align_items": "center",
}


def news_letter():
    return rx.vstack(
        rx.text("Join Newsletter", color="#E8E8F4", style=footer_item_style),
        rx.text(
            "Get the latest updates and news about Reflex.",
            color="#6C6C81",
            font_size="0.8em",
        ),
        rx.chakra.input_group(
            rx.chakra.input_right_element(
                rx.chakra.button(
                    "->",
                    color="#FFF",
                    on_click=IndexState.signup,
                    background="rgba(161, 157, 213, 0.03)",
                    border_left="1px solid rgba(186, 199, 247, 0.12)",
                    border_top_left_radius="0px",
                    border_bottom_left_radius="0px",
                    _hover={"linear-gradient(180deg, #6151F3 0%, #5646ED 100%);"},
                )
            ),
            rx.chakra.input(
                placeholder="you@email.com",
                on_blur=IndexState.set_email,
                color="#fff",
                background="rgba(161, 157, 213, 0.03)",
                border="1px solid rgba(186, 199, 247, 0.12)",
                type="email",
                border_radius="8px",
            ),
            width="100%",
        ),
        align_items="left",
        width="100%",
    )


def links():
    from pcweb.pages.changelog import changelog
    from pcweb.pages.faq import faq

    return rx.hstack(
        rx.desktop_only(
            logo(
                width=["5em", "6em", "7em"],
            ),
        ),
        rx.vstack(
            rx.text("Site"),  # , color="#E8E8F4"
            rx.link("Home", href=index.path, style=footer_item_style),
            rx.link(
                "Changelog",
                href=changelog.path,
                style=footer_item_style,
            ),
            align_items="start",
        ),
        rx.vstack(
            rx.text("Documentation"),
            align_items="start",
        ),
        rx.desktop_only(
            rx.vstack(
                rx.text("Resources"),
                rx.link(
                    "FAQ",
                    href=faq.path,
                    style=footer_item_style,
                ),
                rx.link(
                    "Roadmap",
                    href=constants.ROADMAP_URL,
                    style=footer_item_style,
                ),
                rx.link(
                    "Forum",
                    href=constants.GITHUB_DISCUSSIONS_URL,
                    style=footer_item_style,
                ),
                align_items="start",
            )
        ),
        rx.tablet_and_desktop(
            news_letter(),
        ),
        justify="between",
        align_items="top",
        padding_bottom="2em",
        min_width="100%",
        padding_top="2em",
    )


def footer(style=footer_style):
    return rx.box(
        rx.vstack(
            links(),
            rx.mobile_only(
                news_letter(),
                width="100%",
            ),
            rx.hstack(
                rx.text(
                    "Copyright © 2024 Reflex, Inc.",
                    style=footer_item_style,
                    font_size="0.8em",
                ),
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/companies/light/github.svg",
                            alt="A link to Reflex's Github",
                            height="1.5em",
                        ),
                        href=constants.GITHUB_URL,
                    ),
                    rx.link(
                        rx.image(
                            src="/companies/light/linkedin.svg",
                            alt="A link to Reflex's Linkedin",
                            height="1.5em",
                        ),
                        href=constants.LINKEDIN_URL,
                    ),
                    rx.link(
                        rx.image(
                            src="/companies/light/yc.svg",
                            alt="A link to Reflex's YC profile",
                            height="1.5em",
                        ),
                        href=constants.YC_URL,
                    ),
                    rx.link(
                        rx.image(
                            src="/companies/light/twitter.svg",
                            alt="A link to Reflex's Twitter",
                            height="1.5em",
                        ),
                        href=constants.TWITTER_URL,
                    ),
                    rx.link(
                        rx.image(
                            src="/companies/light/discord.svg",
                            alt="A link to Reflex's Discord",
                            height="1.5em",
                        ),
                        href=constants.DISCORD_URL,
                    ),
                    gap="1em",
                ),
                padding_top="2em",
                justify="between",
                color=rx.color("mauve", 5),
                padding_bottom="2em",
                min_width="100%",
            ),
            padding_x=[".5em", ".5em", ".5em", "2em", "2em", "2em"],
            padding_y=[".5em", ".5em", ".5em", "2em", "2em", "2em"],
            width="100%",
        ),
        # background="#131217",
        width="100%",
        z_index=1,
    )
