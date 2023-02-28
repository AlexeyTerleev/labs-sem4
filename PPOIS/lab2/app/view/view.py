import sys
import os

from kivymd.uix.boxlayout import MDBoxLayout

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.view.components.bar import bar
from app.view.components.table import table

from app.view.components.dialog.add import customer_adding_dialog
from app.view.components.dialog.filter import customer_filter_dialog


class View(MDBoxLayout):
    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.dialog = None

        props = {
            "controller": self.controller
        }

        self.bar = bar(props)
        self.table = table(props)
        self.root = MDBoxLayout(
            self.bar,
            self.table,
            id='root_box',
            orientation='vertical',
        )

    def update(self):

        self.root.remove_widget(self.table)
        self.table = table({
            "controller": self.controller
        })
        self.root.add_widget(self.table)

        print('ALL WIDGETS UPDATED')

    def close_dialog(self):
        self.dialog.dismiss(force=True)

    def open_customer_adding_dialog(self):
        self.dialog = customer_adding_dialog({
            "controller": self.controller
        })
        self.dialog.open()

    def open_customer_filter_dialog(self):
        self.dialog = customer_filter_dialog({
            "controller": self.controller
        })
        self.dialog.open()
        