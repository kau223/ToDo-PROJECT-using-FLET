import flet as ft
from custom_checkbox import Checkbox

def main(page: ft.Page):
    page.title = "Minhas tarefas"
    page.window.width = 400
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)

    def register(e):
        task_list.controls.append(Checkbox(new_task.value))
        page.update()

    new_task = ft.TextField(hint_text="Insira sua tarefa...", expand=True)
    new_buttom = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=register)
    task_list = ft.Column()
    structure = ft.Column(
        controls=[
            ft.Row(controls=[new_task, new_buttom]),
            task_list,
        ]
    )
    page.add(structure)


ft.app(main)
