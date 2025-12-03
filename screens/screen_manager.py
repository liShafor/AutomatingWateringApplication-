from kivy.uix.screenmanager import ScreenManager, SlideTransition
from screens.main_screen import MainScreen
from screens.dashboard_screen import DashboardScreen
from screens.history_screen import HistoryScreen
from screens.settings_screen import SettingsScreen
# from screens.plants_screen import PlantsScreen
# from screens.notes_screen import NotesScreen


class AppScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(duration=0.3)
        self._setup_screens()

    def _setup_screens(self):
        """Инициализация всех экранов"""
        screens = [
            MainScreen(name='main'),
            DashboardScreen(name='dashboard'),
            HistoryScreen(name='history'),
            SettingsScreen(name='settings'),
            # PlantsScreen(name='plants'),
            # NotesScreen(name='notes'),
        ]

        for screen in screens:
            self.add_widget(screen)

    def switch_to(self, screen_name, direction='left'):
        """Универсальный метод переключения экранов"""
        self.transition.direction = direction
        self.current = screen_name
