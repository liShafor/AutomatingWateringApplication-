from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Dashboard"
        self.title = "Главная панель"
        self._setup_ui()

    def _setup_ui(self):
        layout = BoxLayout(orientation="vertical", padding=20)
        content = Label(
            text="Главная панель\n\nЗдесь будет отображаться:\nстатус системы автополива",
            font_size='20sp'
        )
        layout.add_widget(content)

        back_button = Button(
            text="Назад",
            size_hint_y=None,
            height=50
        )
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self):
        if self.manager:
            self.manager.switch_to('main', direction='right')

    # def on_enter(self):
    #     super().on_enter()
    #     self.update_sensor_data()

    def update_sensor_data(self):
        '''arduino connector'''
        pass

    def start_watering(self):
        pass
