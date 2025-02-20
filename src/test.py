import flet as ft

def create_employees():
    row = []
    for i in range(5):
        row.append(ft.Container(
            ft.Column([ft.Text("Петров Адмирал Иванович", size=16, weight=ft.FontWeight.BOLD,
                               color=ft.Colors.WHITE, ), ft.Text("Директор шлагбаума", size=12, color=ft.Colors.WHITE),
                       ft.Text("test@dorogi.ru", size=12, color=ft.Colors.WHITE),
                       ft.Text("+7 233 323 323", size=12, color=ft.Colors.WHITE),
                       ft.Text("15 декабря", size=12, color=ft.Colors.WHITE), ]),
            padding=5,
            bgcolor=ft.colors.GREEN,
            col={"sm": 6, "md": 4, "xl": 2},
        ))
    return row

def main(page: ft.Page):
    page.add(
        ft.ResponsiveRow(
            [
                ft.Text("Сотрудники", weight=ft.FontWeight.BOLD, size=30),
                *create_employees()
                ,
            ]
        )
    )

ft.app(main)