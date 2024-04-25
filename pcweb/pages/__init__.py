from pcweb.route import Route

from .changelog import changelog  # noqa
from .faq import faq  # noqa
from .index import index  # noqa
from .page404 import page404  # noqa

routes = [
    *[r for r in locals().values() if isinstance(r, Route)],
]
