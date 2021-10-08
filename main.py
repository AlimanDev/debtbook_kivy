import os
from typing import NoReturn

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
# from kivy.config import Config
#
# Config.set("graphics", "height", "799")
# Config.set("graphics", "width", "450")

from kivymd.app import MDApp

from View.screens import screens


colors = {
    "Teal": {
        "50": "e4f8f9",
        "100": "bdedf0",
        "200": "97e2e8",
        "300": "79d5de",
        "400": "6dcbd6",
        "500": "6ac2cf",
        "600": "63b2bc",
        "700": "5b9ca3",
        "800": "54888c",
        "900": "486363",
        "A100": "bdedf0",
        "A200": "97e2e8",
        "A400": "6dcbd6",
        "A700": "5b9ca3",
    },
    "Blue": {
        "50": "e3f3f8",
        "100": "b9e1ee",
        "200": "91cee3",
        "300": "72bad6",
        "400": "62acce",
        "500": "589fc6",
        "600": "5191b8",
        "700": "487fa5",
        "800": "426f91",
        "900": "35506d",
        "A100": "b9e1ee",
        "A200": "91cee3",
        "A400": "62acce",
        "A700": "487fa5",
    },
    "Red": {
        "50": "FFEBEE",
        "100": "FFCDD2",
        "200": "EF9A9A",
        "300": "E57373",
        "400": "EF5350",
        "500": "F44336",
        "600": "E53935",
        "700": "D32F2F",
        "800": "C62828",
        "900": "B71C1C",
        "A100": "FF8A80",
        "A200": "FF5252",
        "A400": "FF1744",
        "A700": "D50000",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },
    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    }
}


class DebtBookApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.load_all_kv_files(self.directory)
        self.path_to_view = self.directory + '/View'
        self.load_all_kv_files()
        self.manager_screens = ScreenManager()

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Teal"
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self):
        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

    def load_all_kv_files(self) -> NoReturn:
        for d, dirs, files in os.walk(self.path_to_view):
            for f in files:
                if (
                        os.path.splitext(f)[1] == ".kv"
                        and f != "style.kv"
                        and "Updates" not in d
                        and "__MACOS" not in d
                ):
                    path_to_kv_file = os.path.join(d, f)
                    with open(path_to_kv_file, encoding="utf-8") as kv_file:
                        Builder.load_string(kv_file.read())


DebtBookApp().run()
