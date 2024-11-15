import flet as ft
from flet_route import Routing, path
from pages.page_format import NochkaPage
from pages.page_settings import SettingsPage
from pages.page_tasks import TasksView
from pages.page_info_formatting import Info_formattingPage


class Router:
    def __init__(self, page:ft.Page):
        self.page = page
        self.app_routes = [
            path(url='/', clear=True, view=NochkaPage().view),
            path(url='/settings', clear=False, view=SettingsPage().view),
            path(url='/tasks', clear=False, view=TasksView().view),
            path(url='/info_formatting', clear=False, view=Info_formattingPage().view)
        ]
        Routing(
            page=self.page,
            app_routes=self.app_routes
        )
        self.page.go(self.page.route)