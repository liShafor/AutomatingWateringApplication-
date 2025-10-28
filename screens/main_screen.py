from kivy.uix.screenmanager import ScreenManager, SlideTransition, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main'
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        title = Label(
            text="Умная система автополива",
            font_size='28sp',
            size_hint_y=0.2,
            halign='center',
            bold=True,
            italic=True,
            font_name='Arial',
            color="#1b8db9",
            height=50,
        )
        layout.add_widget(title)

        buttons = [
            ('Панель управления', 'dashboard'),
            ('История', 'history'),
            ('Настройки', 'settings')
        ]

        for text, screen_name in buttons:
            btn = Button(
                text=text,
                font_size='18sp',
                border=(30, 30, 30, 30),
                size_hint_y=None,
                height=60,
                background_color=(0.2, 0.6, 0.3, 1),
                background_normal=''
            )
            btn.screen_name = screen_name
            btn.bind(on_press=self.switch_screen)
            layout.add_widget(btn)

        self.add_widget(layout)

    def switch_screen(self, instance):
        """Переключение на другой экран"""
        if self.manager:
            self.manager.switch_to(instance.screen_name)
