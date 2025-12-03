from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from widgets.particles import ParticleBackground
from widgets.buttons import BackButton, RoundedButton
from screens.main_screen import MainScreen
from screens.autowatering_screen import AutoWateringScreen
from screens.history_screen import HistoryScreen
from screens.plants_screen import PlantsScreen
from screens.documentation_screen import DocumentationScreen

from models.plant import PlantManager
from models.watering_history import HistoryManager


Window.size = (360, 640)


class WateringApp(App):
    def build(self):
        self.load_kv('kv/watering.kv')

        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AutoWateringScreen(name='autowatering'))
        sm.add_widget(HistoryScreen(name='history'))
        sm.add_widget(PlantsScreen(name='plants'))
        sm.add_widget(DocumentationScreen(name='documentation'))

        return sm


if __name__ == '__main__':
    WateringApp().run()
