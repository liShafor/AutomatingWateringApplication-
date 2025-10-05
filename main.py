from kivy.app import App
from app_manager import AppManager


class WateringApp(App):
    def build(self):
        return AppManager()


if __name__ == '__main__':
    WateringApp().run()
