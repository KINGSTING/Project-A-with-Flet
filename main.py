import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = 'Increment Counter'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light'

    textNumber: TextField = TextField(value='0', text_align=ft.TextAlign.RIGHT, width=100)

    def decrement(e: ControlEvent) -> None:
        textNumber.value = str(int(textNumber.value) - 1)
        page.update()

    def increment(e: ControlEvent) -> None:
        textNumber.value = str(int(textNumber.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=decrement),
             textNumber,
             ft.IconButton(ft.icons.ADD, on_click=increment),
             ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
