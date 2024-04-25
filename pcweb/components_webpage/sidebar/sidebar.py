"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx

from pcweb import constants
from pcweb.pages.changelog import changelog
from pcweb.pages.faq import faq


def sidebar(url=None, width: str = "100%") -> rx.Component:
    """Render the sidebar."""

    section_style = {
        "color": "#ffffff",
        "font-weight": "400",
    }

    return rx.vstack(
        rx.link("Changelog", href=changelog.path, style=section_style),
        rx.link(
            "Roadmap",
            href=constants.ROADMAP_URL,
            style=section_style,
        ),
        rx.link(
            "Contribute",
            href=constants.CONTRIBUTING_URL,
            style=section_style,
        ),
        rx.link("FAQ", href=faq.path, style=section_style),
        spacing="5",
        width="100%",
        height="100%",
        justify="end",
    )


sb = sidebar(width="100%")
