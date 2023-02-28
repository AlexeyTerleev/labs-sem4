import sys
import os

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.action import Action


def adding_customer(controller):
    def callback(x):
        controller.dispatch(Action(type_='OPEN_ADDING_DIALOG'))
    return callback


def remove_customers(controller):
    def callback(widget):
        controller.dispatch(Action(type_='REMOVE', content=widget))
    return callback


def filter_table(controller):
    def callback(widget):
        controller.dispatch(Action(type_='OPEN_FILTER_DIALOG', content=widget))
    return callback


def bar(props):
    print("BAR:", props)
    return MDBoxLayout(
        MDRaisedButton(
            text='Add',
            size_hint=(1, 1),
            elevation=0,
            on_press=adding_customer(props['controller'])

        ),
        MDRaisedButton(
            text='Filter',
            size_hint=(1, 1),
            elevation=0,
            on_press=filter_table(props['controller'])
        ),
        MDRaisedButton(
            text='Remove',
            size_hint=(1, 1),
            elevation=0,
            on_press=remove_customers(props['controller'])
        ),
        id='bar',
        size=(200, 100),
        size_hint=(1, None),
        spacing=10,
        padding=10,
    )
