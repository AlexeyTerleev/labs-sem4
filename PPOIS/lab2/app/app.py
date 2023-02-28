import os
import sys

from kivymd.app import MDApp

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.controller import Controller
from app.services.model import Model

import os


class App(MDApp):
    model = None
    controller = None

    def build(self):
        self.title = 'Kono Dio da'
        self.icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "asserts/icon.tiff")
        self.theme_cls.primary_palette = "Teal"

        self.controller = Controller()
        return self.controller.get_view()
