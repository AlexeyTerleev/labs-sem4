from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout


def table(props):
    return MDBoxLayout(
        MDDataTable(
            padding=10,
            elevation=0,
            use_pagination=True,
            pagination_menu_height=330,
            check=True,
            column_data=[
                ("Название турнира", dp(30)),
                ("Дата проведения", dp(30)),
                ("Название вида спорта", dp(60)),
                ("ФИО победителя", dp(30)),
                ("Размер призовых турнира", dp(30)),
                ("Заработок победителя (60% от размера призовых)", dp(30)),
            ],
            row_data=props['controller'].get_customers()

        ),
        id='table_box',
    )