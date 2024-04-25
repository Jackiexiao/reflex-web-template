"""The main Reflex website."""

import reflex as rx

from pcweb import styles
from pcweb.pages import page404, routes
from pcweb.whitelist import _check_whitelisted_path

# This number discovered by trial and error on Windows 11 w/ Node 18, any
# higher and the prod build fails with EMFILE error.
WINDOWS_MAX_ROUTES = 125


# Create the app.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    # theme=rx.theme(has_background=True, radius="large", accent_color="violet"),
)

# Add the pages to the app.
for route in routes:
    if _check_whitelisted_path(route.path):
        app.add_page(
            route.component,
            route.path,
            route.title,
            # image="/previews/index_preview.png",
        )

# Add redirects
redirects = [
    ("/docs", "/docs/getting-started/introduction"),
    ("/docs/getting-started", "/docs/getting-started/introduction"),
]

for source, target in redirects:
    app.add_page(lambda: rx.fragment(), route=source, on_load=rx.redirect(target))

app.add_custom_404_page(page404.component)
