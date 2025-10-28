from kivy.app import App
from kivy.core.window import Window
from screens.screen_manager import AppScreenManager


class AutomaticWateringApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Приложение для автополива"

    def build(self):
        Window.size = (360, 640)
        Window.minimum_width = 360
        Window.minimum_height = 640
        Window.clearcolor = "#2d2d2d"
        return AppScreenManager()

    def on_start(self):
        print(f'Приложение "{self.title}" запущено')

    def on_stop(self):
        print(f'Приложение "{self.title}" закрыто')


if __name__ == '__main__':
    AutomaticWateringApp().run()
