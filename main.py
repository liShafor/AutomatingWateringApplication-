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
from screens.add_plant_screen import AddPlantScreen

import sys
import os

sys.path.append('screens')
sys.path.append('widgets')
sys.path.append('models')

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
        sm.add_widget(AddPlantScreen(name='add_plant'))

        return sm


if __name__ == '__main__':
    WateringApp().run()