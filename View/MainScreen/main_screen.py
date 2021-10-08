from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

from Utility.observer import Observer


class MainScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model.add_observer(self)

    def model_is_changed(self):
        print('MainScreenView')
