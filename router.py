import flet as ft
from flet_route import Routing, path
from pages.Nochka_format import Nochka_Page
from pages.settings import Settings_Page


class Router:
    def __init__(self, page:ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear=True, view=Nochka_Page().view),
            path(url='/settings', clear=False, view=Settings_Page().view)
        ]
        Routing(
            page=self.page,
            app_routes=self.app_routes
        )
        self.page.go(self.page.route)