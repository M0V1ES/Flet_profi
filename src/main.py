from threading import Timer

import flet as ft
from api.api import get_events, get_news


def main(page: ft.Page):

    def create_employees():
        row = []
        for i in range(5):
            row.append(
                ft.Container(
                    ft.Column(
                        [
                            ft.Text(
                                "Петров Адмирал Иванович",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "Директор шлагбаума", size=12, color=ft.Colors.WHITE
                            ),
                            ft.Text("test@dorogi.ru", size=12, color=ft.Colors.WHITE),
                            ft.Text("+7 233 323 323", size=12, color=ft.Colors.WHITE),
                            ft.Text("15 декабря", size=12, color=ft.Colors.WHITE),
                        ]
                    ),
                    padding=5,
                    bgcolor=ft.Colors.GREEN,
                    col={"sm": 6, "md": 4, "xl": 2},
                )
            )
        return row

    def create_events():
        events = []
        data = get_events()
        for value in data:
            events.append(
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.Text(
                                value.title,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                value.description,
                                size=12,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                value.dateTime,
                                size=12,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                value.author,
                                size=12,
                                color=ft.Colors.WHITE,
                            ),
                        ]
                    ),
                    padding=5,
                    width=400,
                    bgcolor=ft.Colors.GREEN,
                    col={"sm": 1, "md": 1, "xl": 1},
                )
            )
        return events

    def create_news():
        news = []
        data = get_news()
        print(data)
        for value in data:
            news.append(
                ft.Container(
                    padding=5,
                    bgcolor=ft.Colors.GREEN,
                    col={"sm": 1, "md": 1, "xl": 1},
                    width=450,
                    height=200,
                    content=ft.Column(
                        controls=[
                            ft.Image(src="./assets/Logo.svg", height=30),
                            ft.Text(
                                value.title,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                value.description,
                                size=12,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                value.dateTime,
                                size=10,
                                text_align=ft.alignment.bottom_left,
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                )
            )
        page.update()
        return news

    page.title = "Web"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Создаем поле для поиска
    search_field = ft.Row(
        controls=[
            ft.TextField(
                hint_text="Введите для поиска",
                expand=True,
                col={"sm": 12, "md": 12, "xl": 12, "xxl": 12},
                border_color=ft.Colors.TRANSPARENT,
                border_radius=10,
                filled=True,
                bgcolor=ft.Colors.WHITE,
                on_submit=lambda e: print(f"Поиск: {e.control.value}"),
            )
        ]
    )

    logo = ft.Image(
        src="Logo.svg",
        width=40,
        height=40,
        fit=ft.ImageFit.CONTAIN,
    )

    # Создаем AppBar с полем поиска
    page.appbar = ft.AppBar(
        leading=logo,  # Логотип в левом углу
        bgcolor=ft.Colors.GREEN,
        actions=[
            ft.Container(content=search_field, padding=ft.padding.only(left=50)),
        ],
    )
    page.add(
        ft.ListView(
            expand=True,
            controls=[
                ft.ResponsiveRow(
                    [
                        ft.Text("Сотрудники", weight=ft.FontWeight.BOLD, size=30),
                        *create_employees(),
                        ft.Row(
                            wrap=True,
                            controls=[
                                ft.Column(
                                    col={"sm": 1, "md": 1, "xl": 1},
                                    controls=[
                                        ft.Text(
                                            "События",
                                            weight=ft.FontWeight.BOLD,
                                            size=30,
                                        ),
                                        *create_events(),
                                    ],
                                ),
                                ft.Column(
                                    col={"sm": 1, "md": 1, "xl": 1},
                                    controls=[
                                        ft.Text(
                                            "Новости",
                                            weight=ft.FontWeight.BOLD,
                                            size=30,
                                        ),
                                        *create_news(),
                                    ],
                                ),
                            ],
                        ),
                    ]
                ),
            ],
        )
    )


ft.app(main, assets_dir="./assets")
