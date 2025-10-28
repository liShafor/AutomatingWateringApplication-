from kivy.uix.screenmanager import Screen


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'splash'
