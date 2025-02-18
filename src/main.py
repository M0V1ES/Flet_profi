import flet as ft
from flet.core.colors import colors
from flet.core.padding import Padding


def main(page):

    page.adaptive = True

    page.title = "Поиск в AppBar"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Создаем поле для поиска
    search_field = ft.TextField(
        hint_text="Введите для поиска",
        expand=False,
        border_color=ft.Colors.TRANSPARENT,
        border_radius=10,
        filled=True,
        bgcolor=ft.Colors.WHITE,
        width=1150,
        on_submit=lambda e: print(f"Поиск: {e.control.value}")
    )

    logo = ft.Image(
        src="./assets/icon.png",
        width=40,
        height=40,
        fit=ft.ImageFit.CONTAIN,
    )

    # Создаем AppBar с полем поиска
    page.appbar = ft.AppBar(
        leading=logo,  # Логотип в левом углу
        bgcolor=ft.Colors.GREEN,

    actions=[
        ft.Container(content=search_field, padding=ft.padding.only(right=30)),
    ],)


    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Bookmark",
            ),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.CupertinoColors.SYSTEM_GREY2, width=0)
        ),
    )
    rows = []
    for i in range(5):
        rows.append(
            ft.Container(bgcolor=ft.Colors.GREEN, width=180, padding=20,
                content=ft.Column(
                    controls=[
                        ft.Text("Петров Адмирал Иванович", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE,),
                        ft.Text("Директор шлагбаума", size=12, color=ft.Colors.WHITE),
                        ft.Text("test@dorogi.ru", size=12, color=ft.Colors.WHITE),
                        ft.Text("+7 233 323 323", size=12, color=ft.Colors.WHITE),
                        ft.Text("15 декабря", size=12, color=ft.Colors.WHITE),
                    ],
                    spacing=1, adaptive=True,
                )
            )
       )
    events=[]
    for i in range(3):
        events.append(ft.Container(bgcolor=ft.Colors.GREEN, width=350, height=100,
                                  content=ft.Column(controls=[
                                     ft.Text("Общее совещание в актовом зале", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                     ft.Text("Все сотрудника отдела 'Администраторы'собираемся", size=12, color=ft.Colors.WHITE),
                                      ft.Text("26.05.2024", size=10, text_align=ft.alignment.bottom_left, color=ft.Colors.WHITE),
                                  ],spacing=1) ))
    news = []
    for i in range(4):
        news.append(ft.Container(bgcolor=ft.Colors.GREEN, width=450, height=100,
                                  content=ft.Column(controls=[
                                     ft.Text("Водители на трассе М-12 сыграли 'Полёт шмеля'", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                     ft.Text("Они ехали-ехали и сыграли! Они ехали-ехали и сыграли! Они ехали ехали и сыграли! Они ехали-ехали и сыграли! Они ехали-ехали и сыграли!", size=12, color=ft.Colors.WHITE),
                                      ft.Text("04.05.2024", size=10, text_align=ft.alignment.bottom_left, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                                  ],spacing=1) ))
    page.add(
        ft.SafeArea(
            ft.Row(controls=[
                    ft.Column(
                    [
                        ft.Text("Сотрудники", weight=ft.FontWeight.BOLD, size=30),
                        ft.Row([
                        *rows,
                        ]),
                        ft.Text("События", weight=ft.FontWeight.BOLD, size=30),
                        ft.Column(
                            [
                                *events,
                            ]
                        )
                    ],
                ),
                ft.Column([
                    ft.Text("Новости", weight=ft.FontWeight.BOLD, size=30),
                    *news
                    ]
            )]
        )

        )
    )


ft.app(main)